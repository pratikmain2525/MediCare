# app/api/consultation_router.py
from fastapi import APIRouter, HTTPException
from typing import List
from core.schema.consultation_schema import ConsultationCreate
from core.services.consultation_service import (
    consultation_create_service,
    get_doctor_consultations_service,
    get_patient_consultations_service
)

consultation_router = APIRouter(prefix="/consultation", tags=["Consultation"])

@consultation_router.post("/")
async def create_consultation_endpoint(payload: ConsultationCreate):
    """
    Create a consultation (all steps in one API)
    """
    return await consultation_create_service(payload)

@consultation_router.get("/doctor/{doctor_id}")
async def get_doctor_consultations_endpoint(doctor_id: int):
    """
    Get all consultations for a doctor
    Doctor can view consultations submitted by patients
    """
    return await get_doctor_consultations_service(doctor_id)

@consultation_router.get("/patient/{patient_id}")
async def get_patient_consultations_endpoint(patient_id: int):
    """
    Get all consultations for a patient
    Patient can view their consultation history
    """
    return await get_patient_consultations_service(patient_id)
