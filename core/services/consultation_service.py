# core/services/consultation_service.py
from core.repository.consultation_repository import (
    create_consultation,
    get_consultations_by_doctor,
    get_consultations_by_patient,
    get_consultation_by_id
)
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

async def consultation_create_service(payload):
    try:
        consultation = await create_consultation(payload.model_dump())
        if not consultation:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create consultation"
            )
        return consultation
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

async def get_doctor_consultations_service(doctor_id: int):
    """Get all consultations for a doctor"""
    try:
        consultations = await get_consultations_by_doctor(doctor_id)
        if not consultations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No consultations found for this doctor"
            )
        return consultations
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

async def get_patient_consultations_service(patient_id: int):
    """Get all consultations for a patient"""
    try:
        consultations = await get_consultations_by_patient(patient_id)
        if not consultations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No consultations found for this patient"
            )
        return consultations
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
