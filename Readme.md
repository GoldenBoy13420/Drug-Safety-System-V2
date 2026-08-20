<div align="center">

# 💊 Drug Safety Intelligence System (V2.0)

### AI-Powered Pharmacovigilance, Risk Assessment & GenAI Platform

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Microservices-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Gemini](https://img.shields.io/badge/Gemini_AI-Pharmacologist-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

[🌟 Overview](#-overview) • [✨ Features](#-features) • [📸 Screenshots](#-screenshots) • [🛠️ Tech Stack](#️-tech-stack) • [📦 Installation](#-installation) • [👨‍💻 Author](#-author)

---

<img src="https://img.icons8.com/fluency/256/000000/pill.png" alt="System Logo" width="120"/>

### **Transform raw clinical data into proactive patient safety insights** ✨

<br/>

[![Frontend](https://img.shields.io/badge/Web_Dashboard-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](/)
[![Backend](https://img.shields.io/badge/REST_API-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](/)
[![Data](https://img.shields.io/badge/FDA_FAERS-2025-blue?style=flat&logo=database&logoColor=white)](/)

</div>

---

## 🌟 Overview

The **Drug Safety Intelligence System (V2.0)** is an end-to-end, AI-powered pharmacovigilance platform. Refactored into a scalable **Microservices Architecture** using Docker, this system analyzes adverse drug events to proactively predict patient harm severity. 

In this major V2 update, the platform goes beyond traditional Machine Learning by integrating **Google's Gemini GenAI** to act as a virtual Clinical Pharmacologist, generating context-aware medical reports based on predictions.

> 🏥 **FDA FAERS Integration** - Built on massive real-world relational databases (Year 2025) including DEMO, DRUG, REAC, THER, and OUTC.

### 🎯 What Makes V2.0 Special?

<table>
<tr>
<td width="50%">

#### 🐳 Microservices Architecture
Fully containerized using **Docker Compose**, separating the frontend UI (Streamlit) from the backend API (FastAPI) for maximum scalability.

#### 🤖 GenAI Clinical Reports
Integrates **Google Gemini 3.6-Flash** to digest patient data and ML predictions, automatically writing professional, actionable clinical advice.

#### 🧠 Advanced ML Models
Utilizes highly optimized **XGBoost** models for both Binary Severity Prediction (ROC-AUC: 85.08%) and Multi-class Reaction Forecasting.

</td>
<td width="50%">

#### ⚡ Automated CI/CD Pipeline
Integrated with **GitHub Actions** for continuous integration, automatically enforcing linting and verifying Docker builds on every push.

#### ⚖️ Class Imbalance Handling
Programmatically tackles real-world clinical data imbalance using strategic downsampling and rigorous Target/Mean Encoding strategies.

#### ☁️ Cloud-Optimized
Refactored from a massive 2GB ensemble to a streamlined **~53MB `joblib`-compressed model**, perfect for strict memory environments.

</td>
</tr>
</table>

---

## ✨ Features

### 📱 Core Modules

<table>
<tr>
<td align="center" width="33%">
<img src="https://img.icons8.com/fluency/96/000000/medical-doctor.png" width="48"/>
<br/><strong>🔬 Patient Risk Analysis</strong>
<br/><sub>Calculates real-time severity probabilities based on patient profiles</sub>
</td>
<td align="center" width="33%">
<img src="https://img.icons8.com/fluency/96/000000/artificial-intelligence.png" width="48"/>
<br/><strong>🤖 AI Pharmacologist</strong>
<br/><sub>Generates actionable medical advice using Google Gemini GenAI</sub>
</td>
<td align="center" width="33%">
<img src="https://img.icons8.com/fluency/96/000000/doctors-bag.png" width="48"/>
<br/><strong>🔮 Reaction Forecasting</strong>
<br/><sub>Predicts the top 3 adverse events a patient might experience</sub>
</td>
</tr>
<tr>
<td align="center">
<img src="https://img.icons8.com/fluency/96/000000/combo-chart.png" width="48"/>
<br/><strong>🚨 Signal Detection</strong>
<br/><sub>Interactive database exploring historical drug-reaction reports</sub>
</td>
<td align="center">
<img src="https://img.icons8.com/fluency/96/000000/api-settings.png" width="48"/>
<br/><strong>⚡ Oriva PV API</strong>
<br/><sub>Containerized FastAPI endpoints for seamless external integration</sub>
</td>
<td align="center">
<img src="https://img.icons8.com/fluency/96/000000/system-report.png" width="48"/>
<br/><strong>📈 Deep EDA Reports</strong>
<br/><sub>High-res clinical pattern visualizations and data drift checks</sub>
</td>
</tr>
</table>

### 🤖 Machine Learning Capabilities

| Task | Algorithm | Optimization | Performance (Test Set) |
|:-----|:----------|:-------------|:-----------------------|
| 🔴 **Severity Prediction** | `XGBClassifier` (Binary) | `scale_pos_weight=1.40`, `tree_method='hist'` | **ROC-AUC: 85.08%**<br>Recall: 77.00% |
| 💊 **Reaction Forecasting** | `XGBClassifier` (Multi-class) | `max_depth=10`, `compress=9` (~53MB footprint) | **Accuracy: 72.85%**<br>(Across 20 targets) |

---

## 📸 Screenshots

<div align="center">

### 💻 Live System Dashboard

<table width="100%">
<tr>
<td align="center" width="50%"><strong>Patient Risk Analysis & GenAI</strong></td>
<td align="center" width="50%"><strong>Global Safety Signals Database</strong></td>
</tr>
<tr>
<td align="center"><img src="frontend/reports/figures/dashboard_preview.png" width="100%" alt="Dashboard Preview"/></td>
<td align="center"><img src="frontend/reports/figures/safety_signals_tab.png" width="100%" alt="Safety Signals Tab"/></td>
</tr>
</table>

### 📊 Deep Exploratory Data Analysis (EDA)

<table width="100%">
<tr>
<td align="center" width="33%"><strong>Demographics (Age/Weight)</strong></td>
<td align="center" width="33%"><strong>Target Imbalance</strong></td>
<td align="center" width="33%"><strong>Top 10 Suspect Drugs</strong></td>
</tr>
<tr>
<td align="center"><img src="frontend/reports/figures/age_weight_distribution.png" width="100%"/></td>
<td align="center"><img src="frontend/reports/figures/target_imbalance.png" width="100%"/></td>
<td align="center"><img src="frontend/reports/figures/top_10_drugs.png" width="100%"/></td>
</tr>
<tr>
<td align="center" colspan="3"><strong>Temporal Stability (Data Drift)</strong></td>
</tr>
<tr>
<td align="center" colspan="3"><img src="frontend/reports/figures/data_drift_check.png" width="80%"/></td>
</tr>
</table>

</div>

---

## 🛠️ Tech Stack

<div align="center">

### Deployment & DevOps
| Technology | Purpose |
|:----------:|---------|
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white) | Containerization & Microservices Orchestration |
| ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white) | CI/CD Pipeline (Linting & Build Tests) |

### Backend, AI & ML
| Technology | Purpose |
|:----------:|---------|
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) | High-performance RESTful API |
| ![Gemini](https://img.shields.io/badge/Google_GenAI-8E75B2?style=flat&logo=google&logoColor=white) | LLM for Clinical Report Generation |
| ![XGBoost](https://img.shields.io/badge/XGBoost-FF9900?style=flat&logo=xgboost&logoColor=white) | Tree-based Classification Algorithms |

### Frontend & Data
| Technology | Purpose |
|:----------:|---------|
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Interactive Web Dashboard |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Clinical Data Manipulation |

</div>

---

## 📦 Installation (Dockerized)

<details>
<summary><strong>📋 Prerequisites</strong></summary>

- ✅ Docker & Docker Compose installed
- ✅ Git installed
- ✅ Google Gemini API Key

</details>

### 🚀 Quick Start

The system is fully containerized. You can launch the entire stack (Frontend + Backend) with a single command.

```bash
# 1️⃣ Clone the repository
git clone [https://github.com/GoldenBoy13420/Drug-Safety-System-V2.git](https://github.com/GoldenBoy13420/Drug-Safety-System-V2.git)
cd Drug-Safety-System-V2
```

**2️⃣ Setup Environment Variables**  
Create a `.env` file in the root directory and add your Gemini API Key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

**3️⃣ Build and Run the Microservices**  

```bash
docker-compose up --build
```

**4️⃣ Access the System**  

- **Frontend Dashboard:** `http://localhost:8501`
- **Backend API Docs (Swagger):** `http://localhost:8000/docs`

---

## 📁 Project Structure (V2.0)

```text
DRUG-SAFETY-SYSTEM-V2/
│
├── 📂 backend/                 # API & AI Microservice
│   ├── 📂 models/              # Compressed XGBoost .pkl models & Encoders
│   ├── main.py                 # FastAPI Endpoints & GenAI Logic
│   ├── Dockerfile
│   └── requirements.txt
│
├── 📂 frontend/                # UI Microservice
│   ├── 📂 reports/             # Safety Signals & EDA Figures
│   ├── app.py                  # Streamlit Dashboard
│   ├── Dockerfile
│   └── requirements.txt
│
├── 📂 .github/workflows/       # CI/CD pipelines (ci.yml)
├── 🐳 docker-compose.yml       # Microservices orchestrator
└── 📄 .gitignore               # Security & Cache exclusions
```

---

## 👨‍💻 Author

<div align="center">

<img src="https://github.com/GoldenBoy13420.png" width="100" style="border-radius: 50%; border: 3px solid #009688; margin-bottom: 15px;"/>

### **Mahmoud Abdelrauf**
*AI & Software Engineer | Pharmacovigilance Systems Developer*

<a href="https://github.com/GoldenBoy13420">
<img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge"/>
</a>

</div>

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ⭐ Support

If you find this AI intelligence architecture helpful, please give it a star!