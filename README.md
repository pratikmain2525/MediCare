# MediCare
# 🏥 MediCare – Backend Service

## 📌 Overview
MediCare is a backend service for an online medical consultation platform designed with clean architecture, scalability, and enterprise-level best practices.

---

## 🎯 Purpose
- Provide APIs for Doctor, Patient
- Support consultation and medical workflows
- Ensure clean separation of concerns

---

## 🛠️ Technology Stack
- Python 3.12  
- FastAPI (REST APIs)  
- SQLAlchemy (ORM)  
- Pydantic (Validation)  
- Poetry (Dependency management) 
- Postgres Database

---

## 🔄 Architecture Flow
```
Client → API Layer → Service Layer → Repository → Database → Response
```

---

## 👥 Roles
- Doctor – Handles consultations
- Patient – Requests consultations

---

## ⚙️ Setup Steps
1. Install dependencies  
   ```bash
   poetry install
   ```

2. Activate virtual environment  
   ```bash
   poetry shell
   ```

3. Configure environment variables in `.env`

4. Run the server  
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 📘 API Documentation
- Swagger UI: http://127.0.0.1:8000/docs  
- ReDoc: http://127.0.0.1:8000/redoc  

---

## ✅ Key Highlights
- Layered and modular architecture  
- Clean, readable, and maintainable code  
- Production-ready backend structure  
- Interview and company-submission friendly  

---

## 🚀 Future Scope
- Doctor verification workflow  
- Appointment scheduling  
- Prescription management  

---

## 👨‍💻 Author
Python Backend Developer
