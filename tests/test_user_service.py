import pytest
from app.services.user_service import register_user
from app.core.security import verify_password


def test_register_user(db_session):
    user = register_user(
        db=db_session,
        email="newuser@example.com",
        password="SecurePass123"
    )

    assert user.id is not None
    assert user.email == "newuser@example.com"
    assert user.hashed_password != "SecurePass123"
    assert verify_password("SecurePass123", user.hashed_password)

def test_register_user_with_existing_email(db_session):
    register_user(
        db=db_session,
        email="duplicate@example.com",
        password="SecurePass123"
    )

    with pytest.raises(ValueError, match="Email already registered"):
        register_user(
            db=db_session,
            email="duplicate@example.com",
            password="AnotherPass123"
        )
