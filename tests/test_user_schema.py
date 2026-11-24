import pytest

from app.schemas.user import UserCreate

def test_user_create_valid_data():
    user = UserCreate(
        email="test@example.com",
        password="Test12345"
    )

    assert user.email == "test@example.com"
    assert user.password == "Test12345"

def test_user_create_password_too_short():
    with pytest.raises(ValueError):
        UserCreate(
            email="test@example.com",
            password="abc123",
        )

def test_user_create_invalid_email():
    with pytest.raises(ValueError):
        UserCreate(
            email="to-nie-jest-email",
            password="Test12345"
        )