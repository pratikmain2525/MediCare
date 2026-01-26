# 🏥 MediCare – Online Medical Consultation Platform

MediCare is a full-stack health-tech application designed to bridge the gap between doctors and patients through a seamless online consultation workflow. Built with a focus on clean architecture, modularity, and scalability, it provides a robust platform for managing medical profiles, consultations, and digital prescriptions.

---

## 📌 Project Overview

MediCare consists of two primary portals:
1.  **Doctor Portal**: Allows medical professionals to manage their profiles and issue digital prescriptions.
2.  **Patient Portal**: Empowers patients to find doctors, view their medical history, and access digital prescriptions securely.

The system is designed with a **Layered Architecture**, ensuring that the user interface, business logic, and database interactions are clearly separated and easy to maintain.

---

## 🚀 Core Features

-   **Dual-Portal System**: Distinct and secure tracks for Doctors and Patients.
-   **Dynamic Profile Management**: Easy-to-use interfaces for updating personal and professional details, including profile picture uploads.
-   **Automated "Dr." Title**: A built-in logic that ensures all medical professionals are correctly addressed.
-   **Digital Prescriptions**: Generate professional, formatted PDF prescriptions that are stored securely and accessible at any time.
-   **Consultation Workflow**: A structured flow from signup to sign-in to the final medical advice.
-   **Unified Look & Feel**: A consistent, premium design across the entire application using modern UI principles.

---

## 📖 How it Works (For Everyone)

Whether you are a healthcare provider or a patient, the system is designed to be intuitive:

### Step 1: Registration (Signup)
New users choose their portal (Doctor or Patient) and fill in their details. Once registered, they are automatically guided to the login page.

### Step 2: Authentication (Sign-in)
Users sign in securely to access their private dashboard.

### Step 3: Profile Setup
Both doctors and patients can upload profile pictures and fill in their background information (Experience/Specialty for Doctors; Age/Medical History for Patients).

### Step 4: Medical Interaction
- **Patients** can browse the list of available specialists.
- **Doctors** can create prescriptions for their patients based on consultations.

### Step 5: Digital Record Keeping
Every prescription is instantly converted into a PDF file that can be downloaded or viewed directly in the browser, ensuring a paperless and reliable medical history.

---

## 🛠️ Technical Deep Dive

### 🎨 Frontend (The User Interface)
The frontend is built for performance and simplicity:
-   **Technologies**: Vanilla Javascript, HTML5, and CSS3.
-   **Architecture**: Multi-page application with dynamic client-side updates.
-   **Interaction**: JavaScript `fetch` API is used for asynchronous communication with the backend, ensuring a smooth user experience without constant page reloads.
-   **Security**: Minimal data is stored in `localStorage` to manage sessions locally.

### ⚙️ Backend (The Engine)
The backend is a modern, high-performance API service:
-   **Framework**: **FastAPI** (Python 3.12+), chosen for its speed and automatic documentation.
-   **Pattern**: **Layered Architecture**:
    -   **Routers**: Handle incoming web requests.
    -   **Services**: Contain the core business logic (e.g., pre-processing data, calling external tools).
    -   **Repositories**: Direct database interaction for data persistence.
    -   **Schemas**: Pydantic models for data validation and API documentation.
-   **Database**: **PostgreSQL** handled via **SQLAlchemy** (Asynchronous ORM).
-   **PDF Engine**: `pdfkit` (running on `wkhtmltopdf`) generates high-quality, formatted medical documents based on HTML templates.

---

## 📂 Folder Structure

```text
MediCare/
├── app/                  # Application Entry & Routers
│   ├── api/              # API Route definitions (Doctor, Patient, etc.)
│   └── main.py           # FastAPI initialization and middleware
├── core/                 # Core Business Logic & Config
│   ├── configs/          # Settings, Database conn, PDF utilities
│   ├── model/            # SQLAlchemy Database Models
│   ├── repository/       # Direct Database Interaction layer
│   ├── schema/           # Pydantic Data Validation Schemas
│   ├── services/         # Complex business logic layer
│   └── templates/        # HTML Templates (Frontend + PDF)
├── storeg/               # Static storage for uploads and PDFs
├── .env                  # Environment configuration
└── pyproject.toml        # Dependency management (Poetry)
```

---

## ⚙️ Setup Instructions

### 1. Prerequisites
- Python 3.12+
- PostgreSQL
- `wkhtmltopdf` (required for PDF generation)

### 2. Installation
1.  **Clone and Install**:
    ```bash
    poetry install
    ```
2.  **Environment Variables**: Create a `.env` file based on the project requirements:
    ```env
    DATABASE_DIALECT=postgresql
    DATABASE_HOSTNAME=localhost
    DATABASE_NAME=medicare
    DATABASE_USERNAME=postgres
    DATABASE_PASSWORD=yourpassword
    DATABASE_PORT=5432
    BASE_STATIC_PATH=storeg/static
    ```

### 3. Run the Application
```bash
uvicorn app.main:app --reload
```

---

## 📘 Interactive Documentation

The system automatically generates professional API documentation:
-   **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
-   **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## ✅ Implementation Highlights

-   **Modular Design**: Every component is decoupled, making the system easy to test and extend.
-   **Robust Error Handling**: Centralized exception handling ensures that users always receive helpful feedback.
-   **Path Consistency**: Profile images and PDFs use a unified path resolution logic, ensuring they work across different environments (Windows/Linux).
-   **Clean Code**: Adheres to PEP 8 standards and uses descriptive naming to ensure even non-authors can understand the flow.

---

**Author**: Antigravity AI Engine
**Collaborator**: Medical Development Team
