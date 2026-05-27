# Smart Asset Management API

Backend REST API for managing enterprise assets and maintenance workflows using FastAPI and SQLAlchemy.

---

## Live API

Swagger Docs:  
https://smart-asset-management-api.onrender.com/docs

---

## Features

- Asset CRUD operations
- Maintenance workflow management
- Asset lifecycle validation
- Filtering, sorting, and pagination
- Overdue asset tracking
- Status-based asset retrieval
- Workflow-driven business rules
- Layered backend architecture

---

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## Architecture

The project follows a layered backend architecture:

```text
Routes → Services → CRUD → SQLAlchemy Models → Database
```

### Layer Responsibilities

- Routes handle API requests and responses
- Services contain workflow logic and business validation
- CRUD layer handles database operations
- SQLAlchemy models manage relational data
- Pydantic schemas handle request/response validation

---

## Project Structure

```text
app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── constants.py
│
├── routes/
│   └── assets.py
│
├── services/
│   └── asset_service.py
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
```

### Navigate to Project

```bash
cd smart-asset-management-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
uvicorn app.main:app --reload
```

### Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## Deployment

Deployed on Render using FastAPI, Uvicorn, and SQLite.

Production URL:  
https://smart-asset-management-api.onrender.com/docs

---

## Main API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /assets/ | Create asset |
| GET | /assets/ | Get all assets |
| GET | /assets/overdue | Get overdue assets |
| GET | /assets/active | Get active assets |
| PUT | /assets/{id} | Update asset |
| DELETE | /assets/{id} | Delete asset |
| POST | /assets/{id}/maintenance | Create maintenance log |

---

## Workflow Rules

- Only active assets can enter maintenance workflow
- Maintenance automatically changes asset status to under_maintenance
- Retired assets cannot be reassigned
- Invalid lifecycle transitions are blocked
- Maintenance due dates cannot be earlier than purchase dates

---

## Swagger Screenshots

### Swagger Overview

<img width="902" height="961" alt="Swagger Overview" src="https://github.com/user-attachments/assets/ef0ac78f-05d2-4793-9479-229d71eb6faf" />

---

### Maintenance Workflow

Demonstration of maintenance workflow execution with real operational data.

### Create Maintenance Request

<img width="1315" height="386" alt="Maintenance Request" src="https://github.com/user-attachments/assets/c8a5e2a2-427e-4719-aada-e007bd4ca51c" />

### Maintenance Workflow Execution

<img width="1318" height="302" alt="Maintenance Execution" src="https://github.com/user-attachments/assets/d5f9f60a-b030-4ed1-8de8-6551afb8e1e5" />

### Successful Maintenance Response

<img width="1315" height="199" alt="Maintenance Response" src="https://github.com/user-attachments/assets/1d1f7f90-3ffa-4bf5-94e4-6ed0147460dd" />

---

### Filtering + Sorting + Pagination

Example query filtering active laptop assets with sorting and paginated results.

### Query Parameters

<img width="395" height="499" alt="Filtering Parameters" src="https://github.com/user-attachments/assets/0ea0bf96-838f-48f2-bcad-ff34558c7ebe" />

### Query Execution

<img width="1185" height="149" alt="Filtering Execution" src="https://github.com/user-attachments/assets/cd24a3c1-7d50-4a78-9ca7-002d09b6ed4a" />

### Paginated Response

<img width="1187" height="215" alt="Filtering Response" src="https://github.com/user-attachments/assets/32219605-2a28-4ec8-a3bf-02d716987f57" />

---

## Future Improvements

- JWT authentication
- PostgreSQL integration
- Automated testing

---
