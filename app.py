import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Student Result Prediction API", version="1.0.0")
model = joblib.load("model/model.joblib")


class StudentInput(BaseModel):
    study_hours: float = Field(..., ge=0, le=24, examples=[6.5])
    attendance: float = Field(..., ge=0, le=100, examples=[85])
    previous_score: float = Field(..., ge=0, le=100, examples=[72])


@app.get("/")
def root():
    return {"message": "Student Result Prediction API is running", "version": "1.0.0"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: StudentInput):
    x = np.array([[data.study_hours, data.attendance, data.previous_score]])
    pred = int(model.predict(x)[0])
    prob = float(model.predict_proba(x)[0][1])
    return {"result": "Pass" if pred == 1 else "Fail", "pass_probability": round(prob, 4)}
