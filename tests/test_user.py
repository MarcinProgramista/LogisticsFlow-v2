from app.models.user import User
from sqlalchemy.exc import IntegrityError
import pytest

def test_create_user():
    user = User(
        email="test@example.com",
        hashed_password="hashed_password_123",
        is_admin=False,
        is_active=True
    )

    assert user.email == "test@example.com"
    assert user.hashed_password == "hashed_password_123"
    assert user.is_admin is False
    assert user.is_active is True

def test_create_user_not_admin(db_session):
    user = User(
        email="admin_test@example.com",
        hashed_password="hashed_password_123",
        is_active=True
    )

    db_session.add(user)
    db_session.flush()

    assert user.is_admin is False
def test_create_user_active(db_session):
    user = User(
        email="test@example.com",
        hashed_password="hashed_password_123",
        is_admin=False,
    )
    db_session.add(user)
    db_session.flush()
    
    assert user.is_active is True

def test_create_user_created_at(db_session):
    user = User(
        email="test@example.com",
        hashed_password="hashed_password_123",
        is_admin=False,
        is_active=True
    )

    db_session.add(user)
    db_session.flush()
    
    assert user.created_at is not None

def test_user_email_must_be_unique(db_session):
    user = User(
        email="test@example.com",
        hashed_password="hashed_password_123",
        is_admin=False,
        is_active=True
    )
    db_session.add(user)
    db_session.flush()

    user_second = User(
        email="test@example.com",
        hashed_password="hashed_password_123",
        is_admin=False,
        is_active=True
    )

    db_session.add(user_second)

    with pytest.raises(IntegrityError):
        db_session.flush()

def test_user_email_required(db_session):
    user = User(
        hashed_password="hashed_password_123",
        is_active=True
    )

    db_session.add(user)
    with pytest.raises(IntegrityError):
        db_session.flush()