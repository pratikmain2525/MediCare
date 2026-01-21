from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL, Enum
from sqlalchemy.orm import relationship, declarative_base
from core.model.BaseModel import BaseModel

class Prescription(BaseModel):
    __tablename__ = "prescriptions"

    prescription_id = Column(Integer, primary_key=True, index=True)
    consultation_id = Column(Integer, ForeignKey("consultations.consultation_id"))

    care_to_be_taken = Column(Text, nullable=False)
    medicines = Column(Text)
    pdf_path = Column(String)

    consultation = relationship(
        "Consultation",
        back_populates="prescription"
    )
