# Gateway System

A **Student Gateway Permission Management System** designed to digitize and simplify student leave and gate-pass requests.

The system provides a role-based approval process involving **Students, Parents, Teachers, and HODs**, reducing manual paperwork and making permission tracking easier.

---

## 🔄 Workflow

### Normal Request

```text id="x8g1w3"
Student
   ↓
Parent Approval
   ↓
Teacher Approval
   ↓
HOD Approval
   ↓
Approved
```

A request can be rejected at any stage.

### Emergency Request

Emergency requests follow a faster approval process after the required parent approval.

---

## 👥 User Roles

| Role        | Responsibility                                |
| ----------- | --------------------------------------------- |
| **Student** | Submit and track requests                     |
| **Parent**  | Approve or reject requests                    |
| **Teacher** | Review requests for assigned students/classes |
| **HOD**     | Provide final departmental approval           |
| **Admin**   | Manage users and system configuration         |

---

## ✨ Features

* Student leave and permission requests
* Multi-level approval workflow
* Emergency request support
* JWT authentication
* Google OAuth
* Role-based access control
* Email notifications
* Request status tracking
* SQLite and PostgreSQL support
* REST API with FastAPI

---

## 🛠️ Technology Stack

| Component         | Technology            |
| ----------------- | --------------------- |
| Backend           | Python, FastAPI       |
| Frontend          | HTML, CSS, JavaScript |
| Database          | SQLite / PostgreSQL   |
| Authentication    | JWT, Google OAuth     |
| Password Security | bcrypt                |
| Email             | SMTP                  |

---

## 📁 Project Structure

```text id="c7xv4z"
Gateway_system/
├── server.py
├── db_connection.py
├── requirements.txt
├── frontend/
├── tests/
├── deployment/
└── .env
```

* **`server.py`** — Main FastAPI backend and API logic.
* **`db_connection.py`** — Database configuration and connection.
* **`frontend/`** — User interface.
* **`tests/`** — Application tests.
* **`requirements.txt`** — Python dependencies.
* **`.env`** — Environment configuration and secrets.

---

## 🚀 Installation

Clone the repository:

```bash id="k5y2b1"
git clone https://github.com/Krithikoduri/Gateway_system.git
cd Gateway_system
```

Create and activate a virtual environment:

```bash id="c2o7pb"
python -m venv venv
```

Install dependencies:

```bash id="6v5n5m"
pip install -r requirements.txt
```

Create a `.env` file:

```env id="6tr8wl"
DATABASE_URL=
JWT_SECRET=

GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

SMTP_HOST=
SMTP_PORT=
SMTP_USERNAME=
SMTP_PASSWORD=
```

Do not commit `.env` or other credentials to GitHub.

---

## ▶️ Run the Application

```bash id="p3z8k4"
uvicorn server:app --reload
```

The backend will be available at:

```text id="7p8k3c"
http://127.0.0.1:8000
```

### API Documentation

Swagger:

```text id="9h1z5k"
http://127.0.0.1:8000/docs
```

ReDoc:

```text id="8p3x2v"
http://127.0.0.1:8000/redoc
```

---

## 🔐 Security

The application uses JWT authentication, password hashing, OAuth, and role-based access control.

Before production deployment:

* Protect all admin endpoints.
* Enforce teacher and HOD authorization.
* Use a strong JWT secret.
* Disable insecure OAuth fallbacks.
* Restrict CORS to trusted domains.
* Use PostgreSQL for production workloads.

---

## 🧪 Testing

The complete workflow should be tested:

```text id="2k7q9m"
Student → Parent → Teacher → HOD → Approved
```

Testing should also cover rejection, authentication failures, unauthorized access, emergency requests, and database operations.

---

## 📌 Project Status

**Development / Pre-production**

The core permission and approval workflow is implemented. Security, authorization, and production configuration should be reviewed before real-world deployment.

---
