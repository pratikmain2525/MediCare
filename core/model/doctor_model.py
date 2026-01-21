from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL, Enum
from sqlalchemy.orm import relationship, declarative_base
from core.model.BaseModel import BaseModel


class Doctor(BaseModel):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True)
    profile_picture = Column(String)
    name = Column(String)
    specialty = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True)
    years_of_experience = Column(DECIMAL(3, 1))

    consultations = relationship("Consultation", back_populates="doctor")