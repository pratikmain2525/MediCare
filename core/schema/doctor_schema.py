from pydantic import BaseModel, EmailStr
from typing import Optional


class DoctorCreate(BaseModel):
    profile_picture: Optional[str] = None
    name: str
    specialty: str
    email: EmailStr
    phone_number: str
    years_of_experience: float


class DoctorLogin(BaseModel):
    email: EmailStr
    phone_number: str


class DoctorResponse(BaseModel):
    doctor_id: int
    profile_picture: Optional[str]
    name: str
    specialty: str
    email: EmailStr
    phone_number: str
    years_of_experience: float

    class Config:
        from_attributes = True

class DoctorProfileResponse(BaseModel):
    doctor_id: int
    name: str
    specialty: str
    years_of_experience: float
    profile_picture: Optional[str]

    class Config:
        from_attributes = True

class DoctorListResponse(BaseModel):
    doctor_id: int
    name: str
    specialty: str
    profile_picture: Optional[str]

    class Config:
        from_attributes = True