from typing import List
from fastapi import APIRouter, File, Form, UploadFile
from core.repository.doctor_repository import get_doctor_profile_picture_service
from core.schema.doctor_schema import DoctorCreate, DoctorListResponse, DoctorLogin, DoctorProfilePicResponse, DoctorProfileResponse, DoctorResponse
from core.services.doctor_service import (
    doctor_profile_picture_update_service,
    doctor_signup_service,
    doctor_signin_service,
    get_doctor_profile_service,
    get_doctors_list_service,
    doctor_logout_service
)

doctor_router = APIRouter(prefix="/doctor", tags=["Doctor"])

@doctor_router.post("/signup")
async def doctor_signup(
    name: str = Form(...),
    specialty: str = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
    years_of_experience: float = Form(...),
    profile_picture: UploadFile | None = File(None)
):
    doctor = DoctorCreate(
        name=name,
        specialty=specialty,
        email=email,
        phone_number=phone_number,
        years_of_experience=years_of_experience
    )
    return await doctor_signup_service(doctor, profile_picture)


@doctor_router.put("/profile-picture/{doctor_id}")
async def update_doctor_picture(
    doctor_id: int,
    profile_picture: UploadFile = File(...)
):
    return await doctor_profile_picture_update_service(
        doctor_id, profile_picture
    )

@doctor_router.post("/signin", response_model=DoctorResponse)
async def doctor_signin(login: DoctorLogin):
    return await doctor_signin_service(login.email, login.phone_number)

@doctor_router.get(
    "/profile/{doctor_id}",
    response_model=DoctorProfileResponse
)
async def doctor_profile(doctor_id: int):
    """
    Doctor Profile Page:
    - Profile Picture
    - Name
    - Specialty
    - Years of Experience
    """
    return await get_doctor_profile_service(doctor_id)

@doctor_router.get(
    "/doctors",
    response_model=List[DoctorListResponse]
)
async def view_doctors_list():
    """
    View Doctors List (Grid Cards)
    - Profile Image
    - Name
    - Specialty
    - Consult Button (frontend)
    """
    return await get_doctors_list_service()

@doctor_router.get(
    "/profile-picture/{doctor_id}",
    response_model=DoctorProfilePicResponse
)
async def get_doctor_profile_picture(doctor_id: int):
    return await get_doctor_profile_picture_service(doctor_id)


@doctor_router.post("/logout/{doctor_id}")
async def doctor_logout(doctor_id: int):
    """
    Doctor Logout
    - Deactivate session
    """
    return await doctor_logout_service(doctor_id)

