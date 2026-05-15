from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List
from datetime import date
import utils

app = FastAPI(title="Medical Registry API by Sakharov Alexander")

class Patient(BaseModel):
    id: int
    full_name: str = Field(..., min_length=2, max_length=100)
    oms_policy: str
    birth_date: date
    email: EmailStr
    gender: str = Field(..., pattern="^(Male|Female)$")

    @field_validator('oms_policy')
    @classmethod
    def check_oms(cls, v: str):
        if not utils.validate_oms_regex(v):
            raise ValueError('OMS policy must be 16 digits')
        return v

db: List[Patient] = []

@app.get("/patients", response_model=List[Patient])
async def get_all_patients():
    return db

@app.post("/patients", status_code=201)
async def create_patient(patient: Patient):
    if any(p.id == patient.id for p in db):
        raise HTTPException(status_code=400, detail="ID already exists")
    db.append(patient)
    return patient

@app.get("/patients/{p_id}")
async def get_patient(p_id: int):
    patient = next((p for p in db if p.id == p_id), None)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.put("/patients/{p_id}")
async def update_patient(p_id: int, updated: Patient):
    for i, p in enumerate(db):
        if p.id == p_id:
            db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Patient not found")

@app.delete("/patients/{p_id}", status_code=204)
async def delete_patient(p_id: int):
    global db
    initial_len = len(db)
    db = [p for p in db if p.id != p_id]
    if len(db) == initial_len:
        raise HTTPException(status_code=404, detail="Patient not found")