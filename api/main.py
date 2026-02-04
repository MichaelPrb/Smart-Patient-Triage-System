import os
from typing import List

# --- Framework Imports ---
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# --- AI & Langchain Imports ---
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------------------------------------------------------------------
# 1. Configuration & Environment
# -------------------------------------------------------------------
load_dotenv() # Load variables from .env file

MY_API_KEY = os.getenv("GOOGLE_API_KEY")

if not MY_API_KEY:
    print("WARNING: GOOGLE_API_KEY not found in .env file. AI features will fail.")

# -------------------------------------------------------------------
# 2. Data Models (Pydantic)
# -------------------------------------------------------------------
class PatientInput(BaseModel):
    gender: str
    age: int
    symptoms: List[str]

class TriageResponse(BaseModel):
    recommended_department: str

class ErrorResponse(BaseModel):
    error: str
    details: str

# -------------------------------------------------------------------
# 3. Initialize FastAPI App
# -------------------------------------------------------------------
app = FastAPI(
    title="Smart-Triage AI System",
    description="AI-powered Backend to recommend medical departments based on patient symptoms.",
    version="1.0.0"
)

# -------------------------------------------------------------------
# 4. AI Chain Initialization
# -------------------------------------------------------------------
# Initialize Gemini Model
model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=MY_API_KEY)

# Define Generic Prompt (Sanitized)
prompt_text = """
You are a professional Medical Triage Assistant AI.
Your task is to recommend ONE specific hospital department based on patient symptoms.
ANSWER ONLY WITH THE DEPARTMENT NAME. No explanation needed.

Examples:
Neurology
Cardiology
Gastroenterology

Patient Info:
- Age: {age}
- Gender: {gender}
- Symptoms: {symptoms}

Recommended Department (One Word):
"""

prompt_template = PromptTemplate.from_template(prompt_text)
chain = prompt_template | model | StrOutputParser()

# -------------------------------------------------------------------
# 5. API Endpoints
# -------------------------------------------------------------------

@app.get("/", summary="System Health Check")
def read_root():
    return {"message": "AI Triage System is running successfully."}

@app.post("/recommend", 
          summary="Get Triage Recommendation", 
          response_model=TriageResponse,
          responses={500: {"model": ErrorResponse}})
def recommend_department(patient_data: PatientInput):
    
    # Convert list of symptoms to string
    symptoms_text = ", ".join(patient_data.symptoms)

    try:
        # Invoke AI Chain
        recommendation = chain.invoke({
            "age": patient_data.age,
            "gender": patient_data.gender,
            "symptoms": symptoms_text
        })
        
        # Clean output
        cleaned_recommendation = recommendation.strip()
        
        return {"recommended_department": cleaned_recommendation}

    except Exception as e:
        print(f"AI Processing Error: {e}")
        return {"error": "Failed to process AI recommendation", "details": str(e)}