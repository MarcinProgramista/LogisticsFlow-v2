import pytest
from unittest.mock import patch
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.services.user_service import register_user, authenticate_user, create_refresh_token
from app.core.security import verify_password, hash_refresh_token
from app.models.refresh_token import RefreshToken

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

def test_register_user_integrity_error(db_session):
    with patch.object(
        db_session,
        "flush",
        side_effect=IntegrityError("INSERT", {}, Exception("Duplicate"))
    ):
        with patch.object(db_session, "rollback") as mock_rollback:
            with pytest.raises(ValueError, match="Email already registered"):
                register_user(
                    db=db_session,
                    email="race@example.com",
                    password="SecurePass123"
                )
            mock_rollback.assert_called_once()

def test_authenticate_user_success(db_session):
    register_user(
        db=db_session,
        email="login@example.com",
        password="SecurePass123"
    )

    user = authenticate_user(
        db=db_session,
        email="login@example.com",
        password="SecurePass123"
    )

    assert user is not None
    assert user.email == "login@example.com"

def test_authenticate_user_wrong_password(db_session):
    register_user(
        db=db_session,
        email="login@example.com",
        password="SecurePass123"
    )

    user = authenticate_user(
        db=db_session,
        email="login@example.com",
        password="WrongPassword123"
    )

    assert user is None

def test_authenticate_user_not_found(db_session):
    user = authenticate_user(
        db=db_session,
        email="unknown@example.com",
        password="SecurePass123"
    )

    assert user is None

def test_authenticate_user_inactive(db_session):
    user = register_user(
        db=db_session,
        email="inactive@example.com",
        password="SecurePass123"
    )

    user.is_active = False
    db_session.flush()

    result = authenticate_user(
        db=db_session,
        email="inactive@example.com",
        password="SecurePass123"
    )

    assert result is None

def test_create_refresh_token(db_session):
    user = register_user(
        db=db_session,
        email="inactive@example.com",
        password="SecurePass123"
    )

    raw_token = create_refresh_token(db_session,user.id)
    result = db_session.execute(
        select(RefreshToken).where(RefreshToken.user_id == user.id)
    )

    saved_token = result.scalar_one_or_none()

    assert saved_token is not None
    assert saved_token.token_hash == hash_refresh_token(raw_token)
    assert saved_token.token_hash != raw_token
