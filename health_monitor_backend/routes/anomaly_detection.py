from fastapi import APIRouter
from pydantic import BaseModel
import joblib

router = APIRouter()

# Load the model
model = joblib.load("../train_model/health_anomaly_model.pkl")

# Define input schema
class Vitals(BaseModel):
    heart_rate: float
    temperature: float
    spo2: float

@router.post("/check-vitals")
def check_vitals(data: Vitals):
    input_data = [[data.heart_rate, data.temperature, data.spo2]]
    result = model.predict(input_data)[0]
    return {
        "status": "anomaly" if result == -1 else "normal",
        "message": "Abnormal readings detected" if result == -1 else "Vitals are within safe range"
    }
