from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.doctor_router import doctor_router
from app.api.patient_router import patient_router
from app.api.consultation_router import consultation_router
from app.api.prescription_router import prescription_router
from app.api.payment_router import payment_router
# from core.configs.database import init_db


import os
from fastapi.staticfiles import StaticFiles

from core.templates.frontend.frontend_router import frontend_router

app = FastAPI(title="MediCare")

# --- Static Storage ---
# Mounting the storeg/static folder to /static URL
BASE_STATIC_PATH = os.getenv("BASE_STATIC_PATH")
app.mount("/static", StaticFiles(directory=BASE_STATIC_PATH), name="static")

# --- CORS Setup ---
origins = [
    "*"  # Allow all, you can restrict to frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allow all HTTP methods
    allow_headers=["*"],  # allow all headers
)

# --- Include Routers ---
app.include_router(frontend_router) # Frontend routes first
app.include_router(doctor_router)
app.include_router(patient_router)
app.include_router(consultation_router)
app.include_router(prescription_router)
app.include_router(payment_router)

# @app.on_event("startup")
# async def startup_event():
#     await init_db()
