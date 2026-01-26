from core.repository.prescription_repository import (
    create_prescription,
    get_prescription_pdf_data,
    update_prescription,
    get_prescription_by_id,
    get_prescriptions_by_patient,
    get_prescription_by_consultation_id
)
from core.configs.pdf_utils import generate_prescription_pdf
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

async def create_prescription_service(payload):
    try:
        # Step 1: Create DB record
        prescription = await create_prescription(payload.model_dump())

        # Step 2: Generate PDF
        pdf_data = await get_prescription_pdf_data(prescription.prescription_id)
        if not pdf_data:
            raise HTTPException(status_code=404, detail="Data for PDF not found")
            
        pdf_path = generate_prescription_pdf(pdf_data)
        
        # Step 3: Update DB with PDF path
        prescription = await update_prescription(prescription.prescription_id, {"pdf_path": pdf_path})
        
        # Final check
        if not prescription or not prescription.pdf_path:
             raise HTTPException(status_code=500, detail="Failed to store PDF path in database")

        return prescription
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"DB Error: {str(e)}")

async def update_prescription_service(prescription_id: int, payload):
    try:
        # Step 1: Fetch prescription
        prescription = await get_prescription_by_id(prescription_id)
        if not prescription:
            raise HTTPException(status_code=404, detail="Prescription not found")

        # Step 2: Update DB
        prescription = await update_prescription(prescription_id, payload.model_dump())

        # Step 3: Regenerate PDF (overwrites old)
        pdf_data = await get_prescription_pdf_data(prescription_id)
        if not pdf_data:
            raise HTTPException(status_code=404, detail="Data for PDF not found")
            
        pdf_path = generate_prescription_pdf(pdf_data)

        # Step 4: Update DB with new PDF path
        prescription = await update_prescription(prescription_id, {"pdf_path": pdf_path})
        
        # Final check
        if not prescription or not prescription.pdf_path:
             raise HTTPException(status_code=500, detail="Failed to store PDF path in database")

        return prescription
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"DB Error: {str(e)}")


async def get_patient_prescriptions_service(patient_id: int):
    prescriptions = await get_prescriptions_by_patient(patient_id)
    if not prescriptions:
        return []  # Return empty list instead of 404 to avoid frontend errors
    return prescriptions

async def get_prescription_by_consultation_id_service(consultation_id: int):
    return await get_prescription_by_consultation_id(consultation_id)
