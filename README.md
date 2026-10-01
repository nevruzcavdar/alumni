# 🎓 Alumni Management System

> **A modern, scalable alumni networking and career platform connecting graduates, students, and institutions.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Local_Dev-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Production-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![AI Assistant](https://img.shields.io/badge/AI_Assistant-Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)

---

## 📌 1. What the System Is

The **Alumni Management System** is an end-to-end web platform designed to bridge the gap between educational institutions and their alumni community. It facilitates lifelong engagement, career development, mentorship opportunities, and professional networking.

### Core Modules & Capabilities:

1. **Alumni Directory & Profiles**
   - Verified graduate profiles detailing graduation year, major, industry, current company, and contact preferences.
   - Search and filter alumni by cohort, location, industry, and skills.

2. **Mentorship & Networking Hub**
   - Connects recent graduates and students with experienced alumni for 1-on-1 mentorship.
   - Direct messaging, guidance scheduling, and career advice channels.

3. **Career & Job Board**
   - Alumni-exclusive job and internship postings.
   - Referral requests and talent recommendations directly within the alumni network.

4. **Events & Reunions**
   - Organization and RSVP tracking for annual alumni meets, webinars, and regional gatherings.
   - Automated event reminders and attendee lists.

5. **Institutional Analytics & Admin Dashboard**
   - Insights into alumni career trajectories, industry distribution, and geographic spread.
   - Verification workflow for new alumni accounts.

---

## 📋 2. Weekly Deliverables & Milestones

| Milestone | Deliverables | Status | Details |
| :--- | :--- | :---: | :--- |
| **Week 1** | Mail & Classroom, Stack Setup, Baseline Routes | ✅ Completed | Python (FastAPI), SQLite/PostgreSQL, Antigravity IDE baseline |
| **Week 2** | **CRUD on `/api/users` + Swagger UI at `/api/swagger`** | ✅ Completed | Full User CRUD lifecycle, SQLite persistence with SQLAlchemy, interactive Swagger UI documentation |

---

## 🛠️ 3. Technology Stack

* **Programming Language:** Python 3.11+ (Fast, modern, type-hinted)
* **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/) (High performance, OpenAPI 3.1, asynchronous)
* **Database:**
  * **Development:** SQLite (`alumni.db` - lightweight local database)
  * **Production:** PostgreSQL (Robust relational database with ACID compliance)
* **ORM:** SQLAlchemy 2.0+
* **Data Validation:** Pydantic v2
* **API Documentation:** Swagger UI (hosted at `/api/swagger`)
* **Testing:** Pytest & FastAPI TestClient (HTTPX)
* **AI Coding Assistant:** [Antigravity IDE](https://deepmind.google/) (Google DeepMind)

---

## 🌐 4. API Endpoints

### 📖 Interactive Documentation
* **Swagger UI:** [http://127.0.0.1:8000/api/swagger](http://127.0.0.1:8000/api/swagger)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* **OpenAPI Schema:** [http://127.0.0.1:8000/api/openapi.json](http://127.0.0.1:8000/api/openapi.json)

### 👥 Users Resource (`/api/users`)
| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :---: |
| `POST` | `/api/users` | Register a new user (alumni, student, faculty, admin) | `201 Created` |
| `GET` | `/api/users` | List users with pagination (`skip`, `limit`) and filters (`role`, `search`) | `200 OK` |
| `GET` | `/api/users/{id}` | Retrieve specific user by ID | `200 OK` |
| `PUT` | `/api/users/{id}` | Update existing user details | `200 OK` |
| `DELETE` | `/api/users/{id}` | Delete user account | `200 OK` |

### 🔍 Utility & Health Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Root status endpoint with project metadata and route links |
| `GET` | `/health` | Liveness health probe |
| `GET` | `/about` | Project overview & author information |
| `GET` | `/hello` | Greeting demo endpoint |
| `GET` | `/sum/{a}/{b}` | Calculation demo endpoint |

---

## 🚀 5. How to Run the System

### Prerequisites

* **Python 3.11+** installed (`python --version`)
* **Git** installed (`git --version`)

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/nevruzcavdar/alumni.git
cd alumni
```

---

### Step 2: Create and Activate a Virtual Environment

* **On Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

* **On macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Configure Environment Variables

```powershell
# Windows
Copy-Item .env.example .env

# macOS / Linux
cp .env.example .env
```

---

### Step 5: Start the Development Server

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Once running, navigate to:
* **Interactive Swagger Documentation:** [http://127.0.0.1:8000/api/swagger](http://127.0.0.1:8000/api/swagger)
* **Users API Endpoint:** [http://127.0.0.1:8000/api/users](http://127.0.0.1:8000/api/users)
* **API Root:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### Step 6: Run Automated Tests

Execute the unit and integration test suite:

```bash
pytest -v
```

---

## 📁 6. Project Structure

```text
alumni/
├── .env.example          # Template for environment configuration
├── .gitignore             # Standard git ignore rules (includes *.db, venv)
├── README.md              # Project documentation, API specs, and run guide
├── requirements.txt       # Project dependencies (FastAPI, SQLAlchemy, Pydantic, etc.)
├── pytest.ini             # Test runner configuration
├── tests/
│   ├── __init__.py
│   └── test_users.py      # Automated tests for CRUD and Swagger UI
└── app/
    ├── __init__.py        # Package initialization
    ├── main.py            # FastAPI entry point & app configuration
    ├── database.py        # SQLAlchemy engine, session maker & DB dependency
    ├── models.py          # SQLAlchemy User entity model
    ├── schemas.py         # Pydantic v2 schemas for User CRUD
    ├── crud.py            # Reusable database CRUD operations
    └── routers/
        ├── __init__.py
        └── users.py       # API route handlers for /api/users
```

---

## 🔄 7. Development Workflow & Commit Cadence

This project adheres strictly to continuous incremental progress:
1. Every feature is structured into modular layers (`models`, `schemas`, `crud`, `routers`).
2. Weekly commitments reflect iterative enhancements: domain models, database migrations, authentication, alumni directory, mentorship workflows, and UI integrations.

---

## 👤 Author

* **Nevruz Çavdar** - [GitHub Profile](https://github.com/nevruzcavdar)
* **Repository:** [nevruzcavdar/alumni](https://github.com/nevruzcavdar/alumni)
