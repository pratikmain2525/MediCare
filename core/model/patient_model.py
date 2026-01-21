from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL, Enum
from sqlalchemy.orm import relationship, declarative_base
from core.model.BaseModel import BaseModel


class Patient(BaseModel):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    profile_picture = Column(String)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True)
    history_of_surgery = Column(Text)
    history_of_illness = Column(Text)

    consultations = relationship("Consultation", back_populates="patient")
