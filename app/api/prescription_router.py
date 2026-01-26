from fastapi import APIRouter
from core.schema.prescription_schema import PrescriptionCreate, PrescriptionUpdate
from core.services.prescription_service import create_prescription_service, update_prescription_service, get_prescription_by_consultation_id_service

prescription_router = APIRouter(prefix="/prescription", tags=["Prescription"])

@prescription_router.post("/")
async def create_prescription_endpoint(payload: PrescriptionCreate):
    """
    Create prescription + generate PDF
    """
    return await create_prescription_service(payload)

@prescription_router.put("/{prescription_id}")
async def update_prescription_endpoint(prescription_id: int, payload: PrescriptionUpdate):
    """
    Update prescription + regenerate PDF
    """
    return await update_prescription_service(prescription_id, payload)

@prescription_router.get("/consultation/{consultation_id}")
async def get_prescription_by_consultation(consultation_id: int):
    """
    Fetch prescription by consultation ID
    """
    return await get_prescription_by_consultation_id_service(consultation_id)
