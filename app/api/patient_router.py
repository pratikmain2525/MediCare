from fastapi import APIRouter, UploadFile, File, Form
from core.schema.patient_schema import PatientCreate, PatientLogin, PatientResponse
from core.services.patient_service import (
    patient_profile_picture_update_service,
    patient_signup_service,
    patient_signin_service,
    patient_logout_service
)

patient_router = APIRouter(prefix="/patient", tags=["Patient"])

@patient_router.post("/signup")
async def patient_signup(
    name: str = Form(...),
    age: int = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
    history_of_surgery: str = Form(None),
    history_of_illness: str = Form(None),
    profile_picture: UploadFile | None = File(None)
):
    patient = PatientCreate(
        name=name,
        age=age,
        email=email,
        phone_number=phone_number,
        history_of_surgery=history_of_surgery,
        history_of_illness=history_of_illness
    )
    return await patient_signup_service(patient, profile_picture)


@patient_router.put("/profile-picture/{patient_id}")
async def update_patient_picture(
    patient_id: int,
    profile_picture: UploadFile = File(...)
):
    return await patient_profile_picture_update_service(
        patient_id, profile_picture
    )



@patient_router.post("/signin", response_model=PatientResponse)
async def patient_signin(login: PatientLogin):
    return await patient_signin_service(login.email, login.phone_number)

@patient_router.post("/logout/{patient_id}")
async def patient_logout(patient_id: int):
    """
    Patient Logout
    - Deactivate session
    """
    return await patient_logout_service(patient_id)
