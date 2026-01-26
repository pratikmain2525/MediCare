from fastapi import APIRouter
from fastapi.responses import HTMLResponse

frontend_router = APIRouter()

@frontend_router.get("/", response_class=HTMLResponse)
async def get_index():
    with open("core/templates/frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/doctor", response_class=HTMLResponse)
async def get_doctor_index():
    # Simple redirect logic or serve a doctor-specific landing page
    # For now, let's redirect to signin as it's the next step in the user's diagram
    with open("core/templates/frontend/doctor/signin.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/doctor/signup", response_class=HTMLResponse)
async def get_doctor_signup():
    with open("core/templates/frontend/doctor/signup.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/doctor/profile", response_class=HTMLResponse)
async def get_doctor_profile_page():
    with open("core/templates/frontend/doctor/profile.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/doctor/consultations", response_class=HTMLResponse)
async def get_doctor_consultations_page():
    with open("core/templates/frontend/doctor/consultations.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/doctor/prescription", response_class=HTMLResponse)
async def get_doctor_prescription_page():
    with open("core/templates/frontend/doctor/prescription.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/doctor/signin", response_class=HTMLResponse)
async def get_doctor_signin():
    with open("core/templates/frontend/doctor/signin.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/patient/signup", response_class=HTMLResponse)
async def get_patient_signup():
    with open("core/templates/frontend/patient/signup.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/patient/signin", response_class=HTMLResponse)
async def get_patient_signin():
    with open("core/templates/frontend/patient/signin.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/patient/doctors", response_class=HTMLResponse)
async def get_patient_doctors_page():
    with open("core/templates/frontend/patient/doctors_list.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/patient/consult", response_class=HTMLResponse)
async def get_patient_consultation_page():
    with open("core/templates/frontend/patient/consultation_form.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/patient/prescriptions", response_class=HTMLResponse)
async def get_patient_prescriptions_page():
    with open("core/templates/frontend/patient/prescriptions.html", "r", encoding="utf-8") as f:
        return f.read()

@frontend_router.get("/patient/profile", response_class=HTMLResponse)
async def get_patient_profile_page():
    with open("core/templates/frontend/patient/profile.html", "r", encoding="utf-8") as f:
        return f.read()
