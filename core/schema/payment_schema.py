from pydantic import BaseModel

class PaymentInitRequest(BaseModel):
    patient_id: int

class PaymentInitResponse(BaseModel):
    payment_id: int
    transaction_id: str
