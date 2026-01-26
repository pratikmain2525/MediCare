from fastapi import HTTPException, UploadFile, status
from core.schema.doctor_schema import DoctorCreate
from core.repository.doctor_repository import (
    get_all_doctors,
    get_doctor_by_email_or_phone,
    create_doctor,
    get_doctor_by_id,
    login_doctor,
    update_doctor_profile_picture,
    logout_doctor,
)

from core.configs.utils import save_profile_picture
from core.configs.settings import get_config

settings = get_config()
DOCTOR_PATH = settings.BASE_STATIC_PATH


async def doctor_signup_service(
    doctor: DoctorCreate,
    profile_picture: UploadFile | None
):
    # 1️⃣ Check if doctor already exists
    existing = await get_doctor_by_email_or_phone(doctor.email, doctor.phone_number)
    if existing:
        return {"message": "Doctor already exists"}

    # 2️⃣ Create doctor WITHOUT profile picture first
    data = doctor.model_dump()
    data["name"] = f"Dr. {data['name']}" if not data["name"].startswith("Dr. ") else data["name"]
    data["profile_picture"] = None
    created_doctor = await create_doctor(data)

    # 3️⃣ Save profile picture if uploaded
    if profile_picture:
        path = save_profile_picture(
            profile_picture,
            base_path=DOCTOR_PATH,
            entity="doctor",
            entity_id=created_doctor.doctor_id
        )
        # 4️⃣ Update DB with new path
        await update_doctor_profile_picture(created_doctor.doctor_id, path)
        created_doctor.profile_picture = path

    return created_doctor

async def doctor_profile_picture_update_service(
    doctor_id: int,
    profile_picture: UploadFile
):
    # 1️⃣ Fetch existing doctor to get old path
    from core.repository.doctor_repository import get_doctor_by_id
    doctor = await get_doctor_by_id(doctor_id)
    if not doctor:
        return {"message": "Doctor not found"}

    # 2️⃣ Save new image, delete old if exists
    path = save_profile_picture(
        profile_picture,
        base_path=DOCTOR_PATH,
        entity="doctor",
        entity_id=doctor_id,
        old_path=doctor.profile_picture  # old file to delete
    )

    # 3️⃣ Update DB
    return await update_doctor_profile_picture(doctor_id, path)


async def doctor_signin_service(email: str, phone_number: str):
    doctor = await login_doctor(email, phone_number)
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or phone number",
        )
    return doctor


async def get_doctor_profile_service(doctor_id: int):
    doctor = await get_doctor_by_id(doctor_id)

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found"
        )

    return doctor

async def get_doctors_list_service():
    doctors = await get_all_doctors()
    return doctors or []

async def get_doctor_profile_picture_service(doctor_id: int):
    doctor = await get_doctor_by_id(doctor_id)

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found"
        )

    return {
        "profile_picture": doctor.profile_picture
    }


async def doctor_logout_service(doctor_id: int):
    doctor = await get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found"
        )
    
    result = await logout_doctor(doctor_id)
    return {"message": "Doctor logged out successfully", "doctor_id": doctor_id}