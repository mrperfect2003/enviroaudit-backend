# FILE PATH

```text
C:\Users\himan\Desktop\EnviroAudit\backend\README.md
```

# FULL README.md CODE

````md
# EnviroAudit Backend

Enterprise ESG Data Ingestion, Normalization, Review and Audit Platform built using Django + Django REST Framework.

---

# Features

## ESG Data Pipeline

- CSV Upload API
- Raw Record Storage
- ESG Normalization Engine
- Scope Mapping (Scope 1, 2, 3)
- Unit Conversion
- Suspicious Record Detection
- Review Workflow
- Audit Trail Logging

---

# Modules

## Organizations

Manage ESG organizations.

### API

```http
GET    /api/organizations/
POST   /api/organizations/
GET    /api/organizations/{id}/
PUT    /api/organizations/{id}/
DELETE /api/organizations/{id}/
```

---

## Ingestion

Upload and process ESG CSV files.

### APIs

```http
GET    /api/ingestion/data-sources/
POST   /api/ingestion/data-sources/

GET    /api/ingestion/imports/
GET    /api/ingestion/raw-records/

POST   /api/ingestion/upload/
```

---

## Normalization

Automatically:

- Normalize units
- Convert quantities
- Map ESG scopes
- Flag suspicious records

### Example

| Activity | Scope |
|---|---|
| Diesel Fuel | Scope 1 |
| Electricity | Scope 2 |
| Flight Travel | Scope 3 |

---

## Review Workflow

Analyst review system for normalized ESG records.

### APIs

```http
GET  /api/review/

POST /api/review/{id}/approve/
POST /api/review/{id}/reject/
POST /api/review/{id}/lock/
```

### Workflow

```text
PENDING
   ↓
APPROVED / REJECTED
   ↓
LOCKED
```

---

## Audit Trail

Tracks all ESG actions and workflow changes.

### API

```http
GET /api/audit/
```

Supports:

- Pagination
- Ordering
- Search

---

# Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend Language |
| Django | Web Framework |
| Django REST Framework | REST APIs |
| SQLite | Database |
| Pandas | CSV Processing |
| UUID | Primary Keys |

---

# Project Structure

```text
backend/
│
├── apps/
│   ├── organizations/
│   ├── ingestion/
│   ├── normalization/
│   ├── review/
│   └── audit/
│
├── config/
├── core/
├── media/
├── manage.py
└── requirements.txt
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Navigate to Backend

```bash
cd backend
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

---

# Run Development Server

```bash
python manage.py runserver
```

Server runs at:

```text
http://127.0.0.1:8000/
```

---

# Admin Panel

```text
http://127.0.0.1:8000/admin/
```

---

# CSV Upload Example

## Endpoint

```http
POST /api/ingestion/upload/
```

## Required Fields

| Field | Type |
|---|---|
| organization_id | UUID |
| source_id | UUID |
| file | CSV File |

---

# Example CSV

```csv
activity_type,quantity,unit
Electricity,500,kWh
Diesel Fuel,200,L
Flight Travel,1200,km
```

---

# Upload Flow

```text
CSV Upload
   ↓
RawRecord Created
   ↓
Normalization Engine
   ↓
NormalizedRecord Created
   ↓
Review Item Created
   ↓
Audit Log Created
```

---

# Suspicious Record Detection

Flags:

- Negative quantities
- Zero quantities
- Extremely large quantities
- Invalid values

---

# Future Improvements

- JWT Authentication
- Multi-Tenant Organizations
- AI Anomaly Detection
- ESG Analytics Dashboard
- Real-Time Notifications
- Report Exporting
- Role-Based Access Control
- Cloud Storage Support

---

# Author

Keshav Raj

Backend Engineer | ESG SaaS Platform Developer

GitHub:
https://github.com/mrperfect2003
````
