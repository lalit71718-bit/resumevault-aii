# ResumeVault AI

## Project Overview

ResumeVault AI is an AI-powered dual-profile career platform designed for both job seekers and recruiters. The platform provides secure authentication, personalized profile management, and scalable backend services using FastAPI and Supabase PostgreSQL. ResumeVault AI simplifies the hiring process by allowing seekers to manage professional profiles and recruiters to discover and connect with suitable candidates efficiently.

---

# Problem Statement

Traditional hiring platforms often lack personalized profile management, secure authentication, and scalable backend architecture. Job seekers struggle to organize and showcase their professional data effectively, while recruiters face difficulties in managing candidate information securely.

ResumeVault AI solves these problems by:

* Providing separate seeker and recruiter profiles
* Offering secure JWT-based authentication
* Enabling scalable cloud database integration with Supabase
* Simplifying profile management through REST APIs
* Creating a modern backend architecture suitable for AI-driven career services

---

# Tech Stack Used

## Backend

* Python
* FastAPI
* Supabase PostgreSQL
* supabase-py
* bcrypt
* python-jose (JWT Authentication)
* Pydantic

## Testing

* Pytest
* HTTPX / FastAPI TestClient

## Tools & Platform

* Git
* GitHub
* VS Code
* Postman

---

# Workflow / Architecture

1. Users register as either a Seeker or Recruiter.
2. Passwords are securely hashed using bcrypt before storing in the database.
3. Users log in through JWT-based authentication.
4. Protected APIs verify JWT tokens using authentication middleware.
5. Based on user roles, the system fetches and updates seeker or recruiter profiles from Supabase PostgreSQL.

### Backend Flow

Client Request → FastAPI Routes → Authentication Middleware → Supabase Database → JSON Response

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/lalit71718-bit/resumevault-aii.git
cd resumevault-aii
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a `.env` file:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## 6. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

## 7. Run Tests

```bash
pytest
```

---

# API Endpoints

| Method | Endpoint        | Description                |
| ------ | --------------- | -------------------------- |
| POST   | /auth/register  | Register new user          |
| POST   | /auth/login     | Login and get JWT token    |
| GET    | /profile/me     | Fetch current user profile |
| PUT    | /profile/update | Update profile details     |

---

# Team Details

## Team Name

Model Makers

## Team Members

* Lalit Kumar Singh
* Eklabay Kumar Adhakari

---

# Future Enhancements

* AI-based resume analysis
* Resume score prediction
* Job recommendation engine
* Recruiter dashboard analytics
* Resume upload and parsing
* Email notifications and interview scheduling

---

# GitHub Repository

Repository Link:

[https://github.com/lalit71718-bit/resumevault-aii](https://github.com/lalit71718-bit/resumevault-aii)
