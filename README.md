# LogisticsFlow

![LogisticsFlow Banner](docs/images/logisticsflow-banner.png)

**LogisticsFlow** is a backend application for transport and logistics management.

The system is designed to support FTL (Full Truck Load) and LTL (Less Than Truckload) operations, including transport orders, cargo, drivers, vehicles and route management.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Pytest

## Main Features

- Customer management
- Transport order management
- Cargo information management
- Multiple pickup and delivery points
- Driver and vehicle management
- Transport assignments
- Route distances and segments
- Transport status monitoring
- Transport event history

## Project Structure

```text
LogisticsFlow/
├── app/
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   ├── database.py
│   └── main.py
├── tests/
├── docs/
│   ├── images/
│   ├── PROJECT_REQUIREMENTS.md
│   ├── DATABASE_DESIGN.md
│   ├── ERD.md
│   └── DEVELOPMENT_PLAN.md
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Documentation

- [Project Requirements](docs/PROJECT_REQUIREMENTS.md)
- [Database Design](docs/DATABASE_DESIGN.md)
- [Entity Relationship Diagram](docs/ERD.md)
- [Development Plan](docs/DEVELOPMENT_PLAN.md)

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd LogisticsFlow
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the database connection using `.env.example` as a reference.

## Running Tests

```bash
pytest
```

## Project Status

**Development – MVP**

The application is being developed incrementally, with tests added alongside each feature.
