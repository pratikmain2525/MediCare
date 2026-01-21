from sqlalchemy import select, or_
from core.configs.database import get_db_connection
from core.model.doctor_model import Doctor
from core.schema.doctor_schema import DoctorCreate


async def get_doctor_by_email_or_phone(email: str, phone_number: str):
    async for db in get_db_connection():
        result = await db.execute(
            select(Doctor).where(
                (Doctor.email == email) | (Doctor.phone_number == phone_number)
            )
        )
        return result.scalar_one_or_none()

async def get_doctor_by_id(doctor_id: int):
    async for db in get_db_connection():
        result = await db.execute(
            select(Doctor).where(Doctor.doctor_id == doctor_id)
        )
        return result.scalar_one_or_none()

async def create_doctor(data: dict):
    async for db in get_db_connection():
        doctor = Doctor(**data)
        db.add(doctor)
        await db.commit()
        await db.refresh(doctor)
        return doctor

async def update_doctor_profile_picture(doctor_id: int, path: str):
    async for db in get_db_connection():
        result = await db.execute(
            select(Doctor).where(Doctor.doctor_id == doctor_id)
        )
        doctor = result.scalar_one_or_none()
        if doctor:
            doctor.profile_picture = path
            await db.commit()
            await db.refresh(doctor)
        return doctor


async def login_doctor(email: str, phone_number: str):
    async for db in get_db_connection():
        result = await db.execute(
            select(Doctor).where(
                Doctor.email == email,
                Doctor.phone_number == phone_number
            )
        )
        doctor = result.scalar_one_or_none()
        if doctor:
            doctor.is_active = True
            await db.commit()
            await db.refresh(doctor)
        return doctor
    
async def get_all_doctors():
    async for db in get_db_connection():
        result = await db.execute(
            select(Doctor)
            .where(Doctor.is_active == True)
            .order_by(Doctor.name)
        )
        return result.scalars().all()

async def logout_doctor(doctor_id: int):
    async for db in get_db_connection():
        result = await db.execute(
            select(Doctor).where(Doctor.doctor_id == doctor_id)
        )
        doctor = result.scalar_one_or_none()
        if doctor:
            doctor.is_active = False
            await db.commit()
            await db.refresh(doctor)
        return doctor
