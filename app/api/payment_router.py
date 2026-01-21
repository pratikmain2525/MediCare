from fastapi import APIRouter
from core.schema.payment_schema import PaymentInitRequest, PaymentInitResponse
from core.services.payment_service import init_payment_service

payment_router = APIRouter(prefix="/payment", tags=["Payment"])

@payment_router.post("/init", response_model=PaymentInitResponse)
async def init_payment(payload: PaymentInitRequest):
    """
    Static / Demo payment init
    """
    return await init_payment_service(payload.patient_id)
