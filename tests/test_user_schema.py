import pytest
from pydantic import ValidationError, field_validator
from app.schemas.user import UserCreate, UserResponse

def test_user_create_valid_data():
    user = UserCreate(
        email="test@example.com",
        password="Test12345"
    )

    assert user.email == "test@example.com"
    assert user.password == "Test12345"

def test_user_create_password_too_short():
    with pytest.raises(ValidationError):
        UserCreate(
            email="test@example.com",
            password="abc123",
        )

def test_user_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            email="to-nie-jest-email",
            password="Test12345"
        )

def test_user_response():
    user = UserResponse(
        id=1,
        email="test@example.com"
    )

    assert user.id == 1
    assert user.email == "test@example.com"
    assert "hashed_password" not in user.model_dump()

def test_user_create_password_too_long():
    data = {
        "email": "test@example.com",
        "password": "A" * 129
    }

    with pytest.raises(ValidationError):
        UserCreate(**data)

def test_user_create_password_only_spaces():
    data = {
        "email": "test@example.com",
        "password": "        "
    }

    with pytest.raises(ValidationError):
        UserCreate(**data)
