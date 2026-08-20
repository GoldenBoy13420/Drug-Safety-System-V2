<div align="center">

# 💊 Drug Safety Intelligence System (V2.0)

### AI-Powered Pharmacovigilance, Risk Assessment & GenAI Platform

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Microservices-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Gemini](https://img.shields.io/badge/Gemini_AI-Pharmacologist-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

<br/>

[🌟 Overview](#-overview) • [✨ Features](#-features) • [🛠️ Tech Stack](#️-tech-stack) • [📦 Installation](#-installation) • [👨‍💻 Author](#-author)

---

<img src="https://img.icons8.com/fluency/256/000000/pill.png" alt="System Logo" width="120"/>

### **Transform raw clinical data into proactive patient safety insights** ✨

</div>

---

## 🌟 Overview

The **Drug Safety Intelligence System (V2.0)** is an end-to-end, AI-powered pharmacovigilance platform. Refactored into a scalable **Microservices Architecture** using Docker, this system analyzes adverse drug events to proactively predict patient harm severity. 

In this major V2 update, the platform goes beyond traditional Machine Learning by integrating **Google's Gemini GenAI** to act as a virtual Clinical Pharmacologist, generating context-aware medical reports based on XGBoost predictions.

> 🏥 **FDA FAERS Integration** - Trained on massive real-world relational databases (Year 2025) including DEMO, DRUG, REAC, THER, and OUTC.

### 🎯 What Makes V2.0 Special?

<table>
<tr>
<td width="50%">

#### 🐳 Microservices Architecture
Fully containerized using **Docker Compose**, separating the frontend UI (Streamlit) from the backend API (FastAPI) for maximum scalability and isolated environments.

#### 🤖 GenAI Clinical Reports
Integrates **Google Gemini 3.6-Flash** to digest patient data and ML predictions, automatically writing professional, actionable clinical pharmacological advice.

#### 🧠 Advanced ML Models
Utilizes highly optimized **XGBoost** models for both Binary Severity Prediction (ROC-AUC: 85.08%) and Multi-class Reaction Forecasting.

</td>
<td width="50%">

#### ⚡ Automated CI/CD Pipeline
Integrated with **GitHub Actions** for continuous integration, automatically enforcing `flake8` linting and verifying Docker builds on every push.

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

---

## 🛠️ Tech Stack

<div align="center">

### Deployment & DevOps
| Technology | Purpose |
|:----------:|---------|
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white) | Containerization & Microservices Orchestration |
| ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white) | CI/CD Pipeline (Linting & Build Tests) |

### Backend & AI
| Technology | Purpose |
|:----------:|---------|
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) | High-performance RESTful API |
| ![Gemini](https://img.shields.io/badge/Google_GenAI-8E75B2?style=flat&logo=google&logoColor=white) | LLM for Clinical Report Generation |
| ![XGBoost](https://img.shields.io/badge/XGBoost-FF9900?style=flat&logo=xgboost&logoColor=white) | Tree-based Classification Algorithms |

### Frontend & Data
| Technology | Purpose |
|:----------:|---------|
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Interactive Web Dashboard |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Clinical Data Manipulation (`pyarrow` backed) |

</div>

---

## 📦 Installation (Dockerized)

<details>
<summary><strong>📋 Prerequisites</strong></summary>

- ✅ Docker & Docker Compose installed and running
- ✅ Git installed
- ✅ Google Gemini API Key

</details>

### 🚀 Quick Start (Recommended)

The system is fully containerized. You can launch the entire stack (Frontend + Backend) with a single command.

**1️⃣ Clone the repository**
```bash
git clone [https://github.com/GoldenBoy13420/Drug-Safety-System-V2.git](https://github.com/GoldenBoy13420/Drug-Safety-System-V2.git)
cd Drug-Safety-System-V2

**2️⃣ Setup Environment Variables**  
Create a `.env` file in the root directory and add your Gemini API Key:

```env
GEMINI_API_KEY=your_actual_api_key_here

**3️⃣ Build and Run the Microservices
docker-compose up --build

**4️⃣ Access the System
Frontend Dashboard: http://localhost:8501
Backend API Docs (Swagger): http://localhost:8000/docs

**📁 Project Structure (V2.0)
DRUG-SAFETY-SYSTEM-V2/
│
├── 📂 backend/                 # API & AI Microservice
│   ├── 📂 models/              # Compressed XGBoost .pkl models & Encoders
│   ├── main.py                 # FastAPI Endpoints & GenAI Logic
│   ├── Dockerfile
│   └── requirements.txt
│
├── 📂 frontend/                # UI Microservice
│   ├── 📂 reports/             # Safety Signals CSV data
│   ├── app.py                  # Streamlit Dashboard
│   ├── Dockerfile
│   └── requirements.txt
│
├── 📂 .github/workflows/       # CI/CD pipelines (ci.yml)
├── 🐳 docker-compose.yml       # Microservices orchestrator
└── 📄 .gitignore               # Security & Cache exclusions

**👨‍💻 Author
Mahmoud Abdelrauf

AI & Software Engineer | Pharmacovigilance Systems Developer

**📜 License
This project is licensed under the MIT License.

**⭐ Support
If you find this AI intelligence architecture helpful, please give it a star!