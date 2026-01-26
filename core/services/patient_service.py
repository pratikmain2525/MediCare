from fastapi import HTTPException, UploadFile, status
from core.schema.patient_schema import PatientCreate
from core.repository.patient_repository import (
    get_patient_by_email_or_phone,
    create_patient,
    get_patient_by_id,
    get_patient_profile_picture_repo,
    login_patient,
    update_patient_profile_picture,
    logout_patient,
)

from core.configs.utils import save_profile_picture
from core.configs.settings import get_config

settings = get_config()
PATIENT_PATH = settings.BASE_STATIC_PATH


async def patient_signup_service(
    patient: PatientCreate, profile_picture: UploadFile | None
):
     # 1️⃣ Check if patient already exists
    existing = await get_patient_by_email_or_phone(patient.email, patient.phone_number)
    if existing:
        return {"message": "Patient already exists"}

    # 2️⃣ Create patient WITHOUT profile picture first
    data = patient.model_dump()
    data["profile_picture"] = None
    created_patient = await create_patient(data)

    # 3️⃣ Save profile picture if uploaded
    if profile_picture:
        path = save_profile_picture(
            profile_picture,
            base_path=PATIENT_PATH,
            entity="patient",
            entity_id=created_patient.patient_id
        )
        # 4️⃣ Update DB with new path
        await update_patient_profile_picture(created_patient.patient_id, path)
        created_patient.profile_picture = path

    return created_patient


async def patient_profile_picture_update_service(
    patient_id: int, profile_picture: UploadFile
):
    # 1️⃣ Fetch existing patient to get old path
    patient = await get_patient_by_id(patient_id)
    if not patient:
        return {"message": "Patient not found"}

    # 2️⃣ Save new image, delete old if exists
    path = save_profile_picture(
        profile_picture,
        base_path=PATIENT_PATH,
        entity="patient",
        entity_id=patient_id,
        old_path=patient.profile_picture  # old file to delete
    )

    # 3️⃣ Update DB
    return await update_patient_profile_picture(patient_id, path)


async def patient_signin_service(email: str, phone_number: str):
    patient = await login_patient(email, phone_number)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or phone number",
        )
    return patient

async def get_patient_profile_picture_service(patient_id: int):
    profile_pic = await get_patient_profile_picture_repo(patient_id)

    if profile_pic is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    return {
        "profile_picture": profile_pic
    }


async def patient_logout_service(patient_id: int):
    patient = await get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    
    result = await logout_patient(patient_id)
    return {"message": "Patient logged out successfully", "patient_id": patient_id}

async def get_patient_profile_service(patient_id: int):
    patient = await get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    return patient
