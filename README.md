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

## 📋 2. Week 1 Deliverables & Contract

As defined in the **Week 1** milestone ("Bring a machine you can work on, pick your stack in the first session without agonising over it, and commit something every single week"):

| Deliverable | Status | Details |
| :--- | :---: | :--- |
| **Mail & Classroom** | ✅ Completed | Communication channels established and verified |
| **Language & Database** | ✅ Completed | Python (FastAPI) + SQLite (Dev) / PostgreSQL (Prod) |
| **AI Assistant** | ✅ Completed | Antigravity IDE (Google DeepMind) |
| **Alumni Repository** | ✅ Completed | Initialized at [`nevruzcavdar/alumni`](https://github.com/nevruzcavdar/alumni) |
| **System Definition & Run Guide**| ✅ Completed | Detailed documentation and runnable baseline in this `README.md` |

---

## 🛠️ 3. Technology Stack

* **Programming Language:** Python 3.11+ (Fast, modern, type-hinted)
* **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/) (High performance, automatic OpenAPI/Swagger documentation, asynchronous)
* **Database:**
  * **Development:** SQLite (Zero-configuration, lightweight local database)
  * **Production:** PostgreSQL (Robust relational database with ACID compliance)
* **ORM & Migrations:** SQLAlchemy 2.0+ & Alembic
* **Data Validation:** Pydantic v2
* **AI Coding Assistant:** [Antigravity IDE](https://deepmind.google/) (Google DeepMind)

---

## 🚀 4. How to Run the System

Follow these instructions to clone, set up, and run the project locally on your machine.

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

Copy the example environment configuration:

* **On Windows (PowerShell):**
  ```powershell
  Copy-Item .env.example .env
  ```

* **On macOS / Linux:**
  ```bash
  cp .env.example .env
  ```

---

### Step 5: Start the Development Server

Launch the FastAPI application with live reload:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Once running, access the services in your browser:

* **API Root:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Interactive Swagger Documentation:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Alternative ReDoc Documentation:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* **Health Check:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

## 📁 5. Project Structure

```text
alumni/
├── .env.example          # Template for environment configuration
├── .gitignore             # Standard git ignore rules for Python & venv
├── README.md              # Project documentation and setup guide
├── requirements.txt       # Project dependencies
└── app/
    ├── __init__.py        # Package initialization
    └── main.py            # FastAPI entry point & API route handlers
```

---

## 🔄 6. Development Workflow & Commit Cadence

This project adheres strictly to continuous incremental progress:
1. Every task is developed on feature branches or committed regularly to `main`.
2. Weekly commitments reflect iterative enhancements: domain models, database migrations, authentication, alumni directory, mentorship workflows, and UI integrations.

---

## 👤 Author

* **Nevruz Çavdar** - [GitHub Profile](https://github.com/nevruzcavdar)
* **Repository:** [nevruzcavdar/alumni](https://github.com/nevruzcavdar/alumni)
