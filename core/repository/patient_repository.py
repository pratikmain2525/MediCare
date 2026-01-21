from core.configs.database import get_db_connection
from core.model.patient_model import Patient
from core.schema.patient_schema import PatientCreate
from sqlalchemy import select, or_

async def get_patient_by_email_or_phone(email: str, phone_number: str):
    async for db in get_db_connection():
        result = await db.execute(
            select(Patient).where(
                (Patient.email == email) | (Patient.phone_number == phone_number)
            )
        )
        return result.scalar_one_or_none()

async def get_patient_by_id(patient_id: int):
    async for db in get_db_connection():
        result = await db.execute(
            select(Patient).where(Patient.patient_id == patient_id)
        )
        return result.scalar_one_or_none()

async def create_patient(data: dict):
    async for db in get_db_connection():
        patient = Patient(**data)
        db.add(patient)
        await db.commit()
        await db.refresh(patient)
        return patient

async def update_patient_profile_picture(patient_id: int, path: str):
    async for db in get_db_connection():
        result = await db.execute(
            select(Patient).where(Patient.patient_id == patient_id)
        )
        patient = result.scalar_one_or_none()
        if patient:
            patient.profile_picture = path
            await db.commit()
            await db.refresh(patient)
        return patient


async def login_patient(email: str, phone_number: str):
    async for db in get_db_connection():
        result = await db.execute(
            select(Patient).where(
                Patient.email == email,
                Patient.phone_number == phone_number
            )
        )
        patient = result.scalar_one_or_none()
        if patient:
            patient.is_active = True
            await db.commit()
            await db.refresh(patient)
        return patient

async def logout_patient(patient_id: int):
    async for db in get_db_connection():
        result = await db.execute(
            select(Patient).where(Patient.patient_id == patient_id)
        )
        patient = result.scalar_one_or_none()
        if patient:
            patient.is_active = False
            await db.commit()
            await db.refresh(patient)
        return patient

