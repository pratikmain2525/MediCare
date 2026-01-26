# core/services/consultation_service.py
from core.repository.consultation_repository import (
    create_consultation,
    get_consultations_by_doctor,
    get_consultations_by_patient,
    get_consultation_by_id
)
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from core.configs.utils import generate_transaction_id

async def consultation_create_service(payload):
    try:
        data = payload.model_dump()
        # Automatically generate transaction ID
        if not data.get("transaction_id"):
            data["transaction_id"] = generate_transaction_id()
            
        consultation = await create_consultation(data)
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
        return await get_consultations_by_doctor(doctor_id) or []
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

async def get_patient_consultations_service(patient_id: int):
    """Get all consultations for a patient"""
    try:
        return await get_consultations_by_patient(patient_id) or []
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

async def get_consultation_by_id_service(consultation_id: int):
    """Get details of a single consultation"""
    try:
        consultation = await get_consultation_by_id(consultation_id)
        if not consultation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Consultation not found"
            )
        return consultation
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
