from pydantic import BaseModel, EmailStr
from typing import Optional

class PatientCreate(BaseModel):
    profile_picture: Optional[str]=None
    name: str
    age: int
    email: EmailStr
    phone_number: str
    history_of_surgery: Optional[str]=None
    history_of_illness: Optional[str]=None


class PatientLogin(BaseModel):
    email: EmailStr
    phone_number: str


class PatientResponse(BaseModel):
    patient_id: int
    profile_picture: Optional[str]
    name: str
    age: int
    email: EmailStr
    phone_number: str
    history_of_surgery: Optional[str]
    history_of_illness: Optional[str]

    class Config:
        from_attributes = True


