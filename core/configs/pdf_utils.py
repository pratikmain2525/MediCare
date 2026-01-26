import pdfkit
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from datetime import datetime

from core.configs.settings import get_config

# Load config
settings = get_config()

# Path to wkhtmltopdf binary
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

# Directory to save PDFs
PDF_DIR = Path(settings.BASE_STATIC_PATH) / "prescription_pdf"
PDF_DIR.mkdir(parents=True, exist_ok=True)

env = Environment(loader=FileSystemLoader("core/templates"))

def generate_prescription_pdf(prescription):
    """
    Generates a PDF from prescription data.
    Overwrites old PDF if exists.
    Returns relative path to PDF.
    """
    template = env.get_template("prescription_template.html")
    
    # Extract data from prescription (could be dict or model object)
    if isinstance(prescription, dict):
        prescription_id = prescription.get("prescription_id")
        care_to_be_taken = prescription.get("care_to_be_taken")
        medicines = prescription.get("medicines") or ""
        patient_name = prescription.get("patient_name")
        doctor_name = prescription.get("doctor_name")
        doctor_specialty = prescription.get("doctor_specialty")
    else:
        prescription_id = prescription.prescription_id
        care_to_be_taken = prescription.care_to_be_taken
        medicines = prescription.medicines or ""
        patient_name = prescription.consultation.patient.name
        doctor_name = prescription.consultation.doctor.name
        doctor_specialty = prescription.consultation.doctor.specialty
    
    html_content = template.render(
        prescription={
            "consultation_id": prescription_id,
            "care_to_be_taken": care_to_be_taken,
            "medicines": medicines,
            "patient_name": patient_name,
            "doctor_name": doctor_name,
            "doctor_specialty": doctor_specialty,
            "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    )

    filename = f"prescription_{prescription_id}.pdf"
    file_path = PDF_DIR / filename

    # Delete old PDF if exists
    if file_path.exists():
        file_path.unlink()

    # PDF generation
    pdfkit.from_string(
        html_content,
        str(file_path),
        configuration=pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    )

    # Return relative path for DB
    return f"static/prescription_pdf/{filename}"
