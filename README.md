# LogisticsFlow

![LogisticsFlow Banner](docs/images/logisticsflow-banner.png)

**LogisticsFlow** is a backend application for transport and logistics management.

The system is designed to support transport operations, including FTL (Full Truck Load) and LTL (Less Than Truckload), transport orders, cargo, customers, drivers, vehicles and route management.

The project combines practical logistics experience with backend development using Python.

## Technology Stack

- Python 3.10
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Pytest
- Git

## Current Implementation

The project currently includes:

- FastAPI application with a health check endpoint
- PostgreSQL database integration
- SQLAlchemy ORM models:
  - Company
  - User
  - Customer
  - Address
  - RouteDistance
- Database migrations using Alembic
- Database constraints and relationships
- Separate test database configuration
- Automated tests using Pytest
- Project documentation

## Current Database Schema

The current database contains five tables:

| Table             | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| `companies`       | Stores company information                                        |
| `users`           | Stores user accounts, hashed passwords and account permissions    |
| `customers`       | Stores customer information and contact details                   |
| `addresses`       | Stores address information                                        |
| `route_distances` | Stores distances and estimated travel durations between addresses |

### Database Relationships and Constraints

- Customers reference addresses through a foreign key.
- Route distances reference two addresses using `address_a_id` and `address_b_id`.
- Unique constraints prevent duplicate address pairs.
- Check constraints prevent a route from referencing the same address as both endpoints.
- User accounts include administrator permissions and an account activation status.
- Passwords are stored as hashes, never as plain text.

### Route Distance Data

The `route_distances` table stores:

- Distance in kilometers.
- Estimated travel duration at 60 km/h.
- Estimated travel duration at 80 km/h.

Travel durations are stored as PostgreSQL `INTERVAL` values.

Database schema changes are managed using Alembic migrations.

## Target System Architecture

The target database architecture is documented in the Entity Relationship Diagram (ERD).

The planned system will include:

- Customers and transport orders
- Order pickup and delivery stops
- Locations
- Transport order events
- Vehicle and driver assignments
- Assignment driver records
- Route segments and route distances

The ERD describes the planned target architecture. Not all entities and relationships have been implemented yet.

See [Entity Relationship Diagram](docs/ERD.md).

## Planned Features

- User registration and authentication
- JWT access and refresh token management
- Company and user management
- Customer management (CRUD)
- Transport order management (CRUD)
- Cargo information management
- Multiple pickup and delivery points
- Driver and vehicle management
- Transport assignments
- Route distance and segment management
- Transport status monitoring
- Transport event history
- Business logic validation
- Automated test coverage

## Project Structure

```text
LogisticsFlow/
├── alembic/
│   ├── versions/
│   └── env.py
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
├── alembic.ini
├── README.md
└── requirements.txt
```

## Documentation

- [Project Requirements](docs/PROJECT_REQUIREMENTS.md)
- [Database Design](docs/DATABASE_DESIGN.md)
- [Entity Relationship Diagram](docs/ERD.md)
- [Development Plan](docs/DEVELOPMENT_PLAN.md)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MarcinProgramista/LogisticsFlow-v2.git
cd LogisticsFlow-v2
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example` and configure the PostgreSQL database connection.

### 5. Run database migrations

```bash
alembic upgrade head
```

## Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API documentation is available at:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Running Tests

Run the automated test suite:

```bash
pytest -v
```

Tests use a separate test database to avoid modifying development data.

## Project Status

**Development – MVP**

The project is being developed incrementally, with automated tests added alongside each feature.

The current focus is on building a reliable database foundation and implementing the core functionality of a transport management system.

## Author

**Marcin Czapla**

Combining 20+ years of logistics experience with backend development in Python.
