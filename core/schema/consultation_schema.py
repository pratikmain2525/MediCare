# core/schema/consultation_schema.py
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class DiabeticsStatus(str, Enum):
    diabetics = "Diabetics"
    non_diabetics = "Non-Diabetics"

class ConsultationCreate(BaseModel):
    patient_id: int = Field(..., description="Patient ID")
    doctor_id: int = Field(..., description="Doctor ID")

    # STEP 1 – Illness
    current_illness_history: Optional[str] = None
    recent_surgery: Optional[str] = None
    surgery_time_span: Optional[str] = None

    # STEP 2 – Medical history
    diabetics_status: Optional[DiabeticsStatus] = None
    allergies: Optional[str] = None
    others: Optional[str] = None

    # STEP 3 – Payment
    transaction_id: Optional[str] = None
    # is_paid: Optional[bool] = False
