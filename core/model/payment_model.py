from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.model.BaseModel import BaseModel

class Payment(BaseModel):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"), nullable=False)
    transaction_id = Column(String, nullable=False)

    patient = relationship("Patient")
