import streamlit as st
import pandas as pd
import requests
import os

# 1. Page Configuration
st.set_page_config(page_title="Drug Safety Intelligence System", layout="wide", initial_sidebar_state="collapsed")

# 2. Custom CSS
st.markdown("""
    <style>
        .block-container { padding-top: 3rem; padding-bottom: 3rem; max-width: 1200px; }
        h1, h3 { font-family: 'Inter', 'Segoe UI', sans-serif; font-weight: 600; }
        
        .stButton>button { 
            background-color: #2563eb; color: #ffffff; border-radius: 8px; 
            border: none; padding: 0.75rem 2rem; font-weight: 600; transition: all 0.3s ease; 
        }
        .stButton>button:hover { background-color: #1d4ed8; color: #ffffff; }

        .result-box-high { 
            padding: 1.5rem; border-radius: 8px; background-color: rgba(239, 68, 68, 0.1); 
            border-left: 4px solid #ef4444; color: #f87171; 
        }
        .result-box-standard { 
            padding: 1.5rem; border-radius: 8px; background-color: rgba(34, 197, 94, 0.1); 
            border-left: 4px solid #22c55e; color: #4ade80; 
        }
        .reaction-box { 
            padding: 1.5rem; border-radius: 8px; background-color: rgba(245, 158, 11, 0.1); 
            border-left: 4px solid #f59e0b; color: #fbbf24; 
        }
        .result-title { font-size: 1.2rem; font-weight: bold; margin-bottom: 0.5rem; display: block; }
        .result-subtitle { font-size: 0.95rem; opacity: 0.9; }
    </style>
""", unsafe_allow_html=True)

# 3. Main Header
st.markdown("<h1>Drug Safety Intelligence System</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Patient Risk Analysis", "Global Safety Signals"])

# ==========================================
# TAB 1: PATIENT RISK ANALYSIS
# ==========================================
with tab1:
    st.markdown("<p style='color: #94a3b8; margin-bottom: 2rem;'>Enter patient and clinical parameters to generate an integrated risk assessment.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("<h3>Patient Demographics</h3>", unsafe_allow_html=True)
        age = st.number_input("Age (Years)", min_value=0, max_value=120, value=50, step=1)
        wt = st.number_input("Weight (KG)", min_value=1.0, max_value=250.0, value=70.0, step=1.0)
        sex = st.selectbox("Sex", ["M", "F", "UNK"])

    with col2:
        st.markdown("<h3>Clinical Data</h3>", unsafe_allow_html=True)
        primary_suspect_drug = st.text_input("Primary Suspect Drug", value="aspirin").lower()
        primary_indication = st.text_input("Primary Indication", value="pain").lower()
        ps_route = st.selectbox("Route of Administration", ["ORAL", "INTRAVENOUS", "SUBCUTANEOUS", "UNKNOWN"])
        num_drugs = st.number_input("Concurrent Drugs", min_value=1, max_value=30, value=1, step=1)
        therapy_duration = st.number_input("Therapy Duration (Days)", min_value=1, max_value=2000, value=30, step=1)

    with col3:
        st.markdown("<h3>Report Metadata</h3>", unsafe_allow_html=True)
        rept_cod = st.selectbox("Report Type", ["EXP", "PER", "UNK"], index=0)
        rpsr_cod = st.selectbox("Report Source", ["SS", "C", "PS", "UNK"], index=0)
        occp_cod = st.selectbox("Reporter Occupation", ["MD", "PH", "LW", "CN", "OT", "UNK"], index=0)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Generate Risk Assessment", use_container_width=True):
        # API URL configuration (supports Docker environment variable)
        API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
        
        payload = {
            'age': age, 'wt': wt, 'num_drugs': num_drugs, 'therapy_duration': therapy_duration, 'num_indications': 1,
            'primary_suspect_drug': primary_suspect_drug, 'ps_route': ps_route, 'primary_indication': primary_indication,
            'rept_cod': rept_cod, 'occp_cod': occp_cod, 'rpsr_cod': rpsr_cod, 'sex': sex
        }

        try:
            with st.spinner("Analyzing patient risk profile via API..."):
                response = requests.post(f"{API_URL}/predict", json=payload)
                
            if response.status_code == 200:
                result = response.json()
                sev_pred = result["severity_prediction"]
                sev_prob = result["severity_probability"]
                top_reactions = result["top_reactions"]

                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<h3>Integrated Assessment Results</h3>", unsafe_allow_html=True)
                
                res_col1, res_col2 = st.columns([1, 1], gap="large")
                
                with res_col1:
                    if sev_pred == 1:
                        st.markdown(f"""
                        <div class='result-box-high'>
                            <span class='result-title'>High Risk Profile Detected</span>
                            Calculated Probability: {sev_prob * 100:.1f}%<br>
                            <span class='result-subtitle'>Patient profile indicates a strong correlation with severe clinical outcomes.</span>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class='result-box-standard'>
                            <span class='result-title'>Standard Risk Profile</span>
                            Calculated Probability: {sev_prob * 100:.1f}%<br>
                            <span class='result-subtitle'>No significant correlation with severe clinical outcomes detected.</span>
                        </div>
                        """, unsafe_allow_html=True)

                with res_col2:
                    reactions_html = "<div class='reaction-box'><span class='result-title'>Predicted Adverse Events</span><ul style='margin-top: 10px; margin-bottom: 0;'>"
                    for rx in top_reactions:
                        reaction_name = rx["name"].title()
                        confidence = rx["probability"] * 100
                        reactions_html += f"<li><strong>{reaction_name}</strong> (Confidence: {confidence:.1f}%)</li>"
                    reactions_html += "</ul></div>"
                    
                    st.markdown(reactions_html, unsafe_allow_html=True)
                
                # --- NEW SECTION: Generative AI Clinical Report ---
                ai_report = result.get("clinical_report", "")
                if ai_report:
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("<h3>🤖 AI Clinical Pharmacologist Report</h3>", unsafe_allow_html=True)
                    st.info(ai_report)

            else:
                st.error(f"API Error: {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("🚨 Connection Error: Cannot connect to the FastAPI backend. Ensure the server is running.")

# ==========================================
# TAB 2: GLOBAL SAFETY SIGNALS
# ==========================================
with tab2:
    st.markdown("<p style='color: #94a3b8; margin-bottom: 2rem;'>Historical drug-adverse event pairs requiring clinical investigation.</p>", unsafe_allow_html=True)
    try:
        # المسار الجديد بعد ما ربطناه بالـ Docker
        df_signals = pd.read_csv('reports/safety_signals_report.csv')
        
        search_drug = st.text_input("Search Database by Drug Name:", "").lower()
        display_df = df_signals[df_signals['drug'].str.lower().str.contains(search_drug)] if search_drug else df_signals
        st.dataframe(display_df, use_container_width=True, height=500)
    except Exception:
        st.warning("Safety signals report not found. You can run the data pipeline to generate it.")