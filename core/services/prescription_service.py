from core.repository.prescription_repository import (
    create_prescription,
    get_prescription_pdf_data,
    update_prescription,
    get_prescription_by_id
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
        pdf_path = generate_prescription_pdf(pdf_data)
        # Step 3: Update DB with PDF path
        prescription = await update_prescription(prescription.prescription_id, {"pdf_path": pdf_path})

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
        pdf_path = generate_prescription_pdf(prescription)

        # Step 4: Update DB with new PDF path
        prescription = await update_prescription(prescription_id, {"pdf_path": pdf_path})

        return prescription
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"DB Error: {str(e)}")
