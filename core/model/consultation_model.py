from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL, Enum
from sqlalchemy.orm import relationship, declarative_base
from core.model.BaseModel import BaseModel

class Consultation(BaseModel):
    __tablename__ = "consultations"

    consultation_id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.patient_id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"), nullable=False)

    # STEP 1 – Illness
    current_illness_history = Column(Text, nullable=True)
    recent_surgery = Column(Text, nullable=True)
    surgery_time_span = Column(String, nullable=True)

    # STEP 2 – Medical history
    diabetics_status = Column(
        Enum("Diabetics", "Non-Diabetics", name="diabetics_status"),
        nullable=True
    )
    allergies = Column(Text, nullable=True)
    others = Column(Text, nullable=True)

    # STEP 3 – Payment
    transaction_id = Column(String, nullable=True)
    # is_paid = Column(Boolean, default=False)

    # Relationships
    patient = relationship("Patient", back_populates="consultations")
    doctor = relationship("Doctor", back_populates="consultations")
    prescription = relationship(
        "Prescription", 
        back_populates="consultation", 
        uselist=False
    )


# class Consultation(BaseModel):
#     __tablename__ = "consultations"

#     consultation_id = Column(Integer, primary_key=True, index=True)
#     patient_id = Column(Integer, ForeignKey("patients.patient_id"))
#     doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"))

#     current_illness_history = Column(Text)
#     recent_surgery = Column(Text)
#     surgery_time_span = Column(String)

#     diabetics_status = Column(Enum("Diabetics", "Non-Diabetics", name="diabetics_status"))
#     allergies = Column(Text)
#     others = Column(Text)

#     transaction_id = Column(String)

#     patient = relationship("Patient", back_populates="consultations")
#     doctor = relationship("Doctor", back_populates="consultations")

#     prescription = relationship("Prescription", back_populates="consultation", uselist=False)
#     payment = relationship("Payment", back_populates="consultation", uselist=False)