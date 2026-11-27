import os
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import Address, Customer
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from app.models.user import User
from app.models.refresh_token import RefreshToken

load_dotenv()

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

if TEST_DATABASE_URL is None:
    raise ValueError("TEST_DATABASE_URL is not set")

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine 
)

Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    session = TestingSessionLocal()
    session.execute(delete(RefreshToken))
    session.execute(delete(User))
    session.commit()
    try:
        yield session
    finally:
        session.rollback()
        session.close()

@pytest.fixture
def override_get_db(db_session):
    def _override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = _override_get_db
    yield
    app.dependency_overrides.clear()

@pytest.fixture
def client(override_get_db):
    return TestClient(app)

