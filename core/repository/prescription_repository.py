from sqlalchemy import select
from core.configs.database import get_db_connection
from core.model.prescription_model import Prescription
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload
from core.model.consultation_model import Consultation

async def create_prescription(data: dict):
    async for db in get_db_connection():
        try:
            prescription = Prescription(**data)
            db.add(prescription)
            await db.commit()
            await db.refresh(prescription)
            return prescription
        except SQLAlchemyError as e:
            await db.rollback()
            raise e

async def update_prescription(prescription_id: int, data: dict):
    async for db in get_db_connection():
        result = await db.execute(
            select(Prescription).where(Prescription.prescription_id == prescription_id)
        )
        prescription = result.scalar_one_or_none()
        if prescription:
            for key, value in data.items():
                setattr(prescription, key, value)
            await db.commit()
            await db.refresh(prescription)
        return prescription

async def get_prescription_by_id(prescription_id: int):
    async for db in get_db_connection():
        result = await db.execute(
            select(Prescription)
            .options(
                selectinload(Prescription.consultation)
                .selectinload(Consultation.doctor),
                selectinload(Prescription.consultation)
                .selectinload(Consultation.patient),
            )
            .where(Prescription.prescription_id == prescription_id)
        )
        return result.scalar_one_or_none()
    

async def get_prescription_pdf_data(prescription_id: int):
    async for db in get_db_connection():
        result = await db.execute(
            select(Prescription)
            .options(
                selectinload(Prescription.consultation)
                .selectinload(Consultation.doctor),
                selectinload(Prescription.consultation)
                .selectinload(Consultation.patient),
            )
            .where(Prescription.prescription_id == prescription_id)
        )
        prescription = result.scalar_one_or_none()
        if not prescription:
            return None

        return {
            "prescription_id": prescription.prescription_id,
            "care_to_be_taken": prescription.care_to_be_taken,
            "medicines": prescription.medicines or "",
            "patient_name": prescription.consultation.patient.name,
            "doctor_name": prescription.consultation.doctor.name,
            "doctor_specialty": prescription.consultation.doctor.specialty,
        }

async def get_prescriptions_by_doctor(doctor_id: int):
    """Get all prescriptions written by a doctor"""
    async for db in get_db_connection():
        result = await db.execute(
            select(Prescription)
            .options(
                selectinload(Prescription.consultation)
                .selectinload(Consultation.patient),
                selectinload(Prescription.consultation)
                .selectinload(Consultation.doctor),
            )
            .join(Consultation)
            .where(Consultation.doctor_id == doctor_id)
            .order_by(Prescription.created_at.desc())
        )
        return result.scalars().all()

async def get_prescriptions_by_patient(patient_id: int):
    """Get all prescriptions for a patient"""
    async for db in get_db_connection():
        result = await db.execute(
            select(Prescription)
            .options(
                selectinload(Prescription.consultation)
                .selectinload(Consultation.patient),
                selectinload(Prescription.consultation)
                .selectinload(Consultation.doctor),
            )
            .join(Consultation)
            .where(Consultation.patient_id == patient_id)
            .order_by(Prescription.created_at.desc())
        )
        return result.scalars().all()

async def get_prescription_by_consultation_id(consultation_id: int):
    """Get a prescription by its consultation ID"""
    async for db in get_db_connection():
        result = await db.execute(
            select(Prescription)
            .where(Prescription.consultation_id == consultation_id)
        )
        return result.scalar_one_or_none()
