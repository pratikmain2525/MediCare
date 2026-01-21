from pydantic import BaseModel
from typing import Optional

class PrescriptionCreate(BaseModel):
    consultation_id: int
    care_to_be_taken: str
    medicines: Optional[str] = None

class PrescriptionUpdate(BaseModel):
    care_to_be_taken: Optional[str] = None
    medicines: Optional[str] = None
