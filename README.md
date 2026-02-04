# 🏥 Smart Patient Triage System (AI-Powered)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)
![AI](https://img.shields.io/badge/AI-Gemini%20Pro-orange)

An end-to-end medical triage solution designed to automate patient risk analysis and department recommendations using **Generative AI (LLM)**.

## 🚀 Project Overview

This system helps hospital administration reduce manual triage time by:
1.  **Analyzing High-Risk Patients:** Processing EMR data to identify patients with critical symptoms.
2.  **Automating SQL Insights:** Querying complex patient-visit relationships.
3.  **AI Recommendation Engine:** Using Google Gemini to classify symptoms into specific medical departments (Neurology, Cardiology, etc.).

## 📂 Repository Structure

```text
├── api/                  # Backend API (FastAPI + LangChain)
│   ├── main.py           # Application Entry Point
│   └── requirements.txt  # Dependencies
├── notebooks/            # Data Science Modules
│   └── 01_patient_risk_analysis.ipynb  # Feature Engineering & Filtering Logic
└── sql_queries/          # Database Analytics
    └── high_risk_patient_query.sql     # Complex SQL Query for Risk Assessment
```

🛠️ Tech Stack
Language: Python 3.10+

Backend: FastAPI, Uvicorn

AI/LLM: LangChain, Google Gemini Pro

Data Processing: Pandas

Database: SQL (PostgreSQL Syntax Compatible)

💻 How to Run the AI API
Clone the repository:

Bash
git clone [https://github.com/USERNAME_GITHUB/Smart-Patient-Triage-System.git](https://github.com/USERNAME_GITHUB/Smart-Patient-Triage-System.git)
cd Smart-Patient-Triage-System
Install Dependencies:

Bash
pip install -r api/requirements.txt
Setup Environment Variables: Create a .env file in the api/ folder and add your API Key:

Code snippet
GOOGLE_API_KEY=your_gemini_api_key_here
Run the Server:

Bash
uvicorn api.main:app --reload
Access the API Documentation at: http://127.0.0.1:8000/docs

Created by Michael Emmanuel Purba


---

### 🚀 Push README ke GitHub

Setelah file `README.md` disimpan, lakukan ritual terakhir di Git Bash:

```bash
git add README.md
git commit -m "docs: add professional documentation"
git push