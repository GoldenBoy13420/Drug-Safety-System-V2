from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os
from google import genai
from dotenv import load_dotenv

# 1. Load Environment Variables (API Key)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Initialize the NEW Google Gen AI Client
llm_client = None
if GEMINI_API_KEY:
    try:
        # The new SDK automatically picks up GEMINI_API_KEY from environment or you can pass it explicitly
        llm_client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"Failed to initialize Gemini Client: {e}")
else:
    print("WARNING: GEMINI_API_KEY not found in .env file!")

app = FastAPI(title="Drug Safety Intelligence API", version="2.0")

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

try:
    sev_model = joblib.load(os.path.join(MODEL_DIR, 'xgb_severity_model.pkl'))
    sev_encoders = joblib.load(os.path.join(MODEL_DIR, 'severity_encoders.pkl'))
    reac_model = joblib.load(os.path.join(MODEL_DIR, 'xgb_matrix_b_model.pkl'))
    reac_le = joblib.load(os.path.join(MODEL_DIR, 'le_matrix_b.pkl'))
    reac_oe = joblib.load(os.path.join(MODEL_DIR, 'oe_matrix_b.pkl'))
except Exception as e:
    print(f"Error loading models: {e}")

class PatientInput(BaseModel):
    age: int
    wt: float
    num_drugs: int
    therapy_duration: int
    num_indications: int = 1
    primary_suspect_drug: str
    ps_route: str
    primary_indication: str
    rept_cod: str
    occp_cod: str
    rpsr_cod: str
    sex: str

@app.get("/")
def read_root():
    return {"status": "Backend API is up and running!"}

@app.post("/predict")
def predict_risk(data: PatientInput):
    try:
        input_dict = data.dict()
        df_input = pd.DataFrame([input_dict])

        # --- 1. Severity Logic ---
        df_sev = df_input.copy()
        for col in ['primary_suspect_drug', 'ps_route', 'primary_indication']:
            val = df_sev[col].iloc[0]
            df_sev[col + '_encoded'] = sev_encoders[col].get(val, sev_encoders['overall_mean']) if col in sev_encoders else sev_encoders['overall_mean']
            df_sev.drop(columns=[col], inplace=True)
            
        df_sev = pd.get_dummies(df_sev, columns=['sex'])
        for c in set(sev_encoders['train_columns']) - set(df_sev.columns): 
            df_sev[c] = 0
        df_sev = df_sev[sev_encoders['train_columns']]
        
        sev_pred = int(sev_model.predict(df_sev)[0])
        sev_prob = float(sev_model.predict_proba(df_sev)[0][1])
        risk_level = "High Risk" if sev_pred == 1 else "Standard Risk"

        # --- 2. Reaction Logic ---
        df_reac = df_input.copy()
        cat_cols = ['primary_suspect_drug', 'ps_route', 'rept_cod', 'occp_cod', 'rpsr_cod', 'primary_indication', 'sex']
        df_reac[cat_cols] = df_reac[cat_cols].astype(str)
        df_reac[cat_cols] = reac_oe.transform(df_reac[cat_cols])
        
        expected_cols = ['age', 'wt', 'sex', 'occp_cod', 'rept_cod', 'primary_suspect_drug', 'ps_route', 'num_drugs', 'therapy_duration', 'rpsr_cod', 'num_indications', 'primary_indication']
        df_reac = df_reac[expected_cols]
        
        reac_probs = reac_model.predict_proba(df_reac)[0]
        top_3_idx = reac_probs.argsort()[-3:][::-1]

        top_reactions = []
        reaction_names = []
        for idx in top_3_idx:
            reaction_name = reac_le.inverse_transform([idx])[0]
            confidence = float(reac_probs[idx])
            top_reactions.append({"name": reaction_name, "probability": confidence})
            reaction_names.append(reaction_name)

        # --- 3. Generative AI Logic (Gemini - New SDK) ---
        clinical_report = "Clinical report unavailable. Please check API Key."
        if llm_client:
            prompt = f"""
            You are an expert clinical pharmacologist. Analyze the following patient data and machine learning predictions to write a concise, professional clinical warning/recommendation for the prescribing physician.
            
            Patient: {data.age} years old, Weight: {data.wt} kg.
            Prescribed Drug: {data.primary_suspect_drug} (for {data.primary_indication}).
            Concurrent Drugs: {data.num_drugs}.
            
            Our ML model predicts a {risk_level} profile with a {sev_prob * 100:.1f}% probability of severe adverse events.
            Top predicted side effects: {', '.join(reaction_names)}.
            
            Write a 3-sentence professional clinical recommendation advising the doctor on how to monitor or proceed with this patient. Do not use generic disclaimers. Focus on medical actionability.
            """
            try:
                # Using the new interactions.create syntax for the modern SDK
                interaction = llm_client.interactions.create(
                    model="gemini-3.6-flash",
                    input=prompt
                )
                clinical_report = interaction.output_text
            except Exception as e:
                clinical_report = f"Generative AI error: {str(e)}"

        return {
            "severity_prediction": sev_pred,
            "severity_probability": sev_prob,
            "top_reactions": top_reactions,
            "clinical_report": clinical_report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))