# core/repository/consultation_repository.py
from sqlalchemy import select
from core.configs.database import get_db_connection
from core.model.consultation_model import Consultation
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

async def create_consultation(data: dict):
    async for db in get_db_connection():
        try:
            consultation = Consultation(**data)
            db.add(consultation)
            await db.commit()
            await db.refresh(consultation)
            return consultation
        except SQLAlchemyError as e:
            await db.rollback()
            raise e

async def get_consultations_by_doctor(doctor_id: int):
    """Get all consultations for a doctor"""
    async for db in get_db_connection():
        result = await db.execute(
            select(Consultation)
            .options(
                selectinload(Consultation.patient),
                selectinload(Consultation.doctor)
            )
            .where(Consultation.doctor_id == doctor_id)
            .order_by(Consultation.created_at.desc())
        )
        return result.scalars().all()

async def get_consultations_by_patient(patient_id: int):
    """Get all consultations for a patient"""
    async for db in get_db_connection():
        result = await db.execute(
            select(Consultation)
            .options(
                selectinload(Consultation.patient),
                selectinload(Consultation.doctor)
            )
            .where(Consultation.patient_id == patient_id)
            .order_by(Consultation.created_at.desc())
        )
        return result.scalars().all()

async def get_consultation_by_id(consultation_id: int):
    """Get a specific consultation"""
    async for db in get_db_connection():
        result = await db.execute(
            select(Consultation)
            .options(
                selectinload(Consultation.patient),
                selectinload(Consultation.doctor)
            )
            .where(Consultation.consultation_id == consultation_id)
        )
        return result.scalar_one_or_none()