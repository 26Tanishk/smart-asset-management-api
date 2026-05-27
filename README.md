# Smart Asset Management API
Backend REST API for managing enterprise assets and maintenance workflows using FastAPI and SQLAlchemy.

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
Screenshots demonstrating API workflows and validation behavior.
---

## Future Improvements

- JWT authentication
- PostgreSQL integration
- Automated testing


---
