from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from datetime import datetime, timedelta, timezone
from app.models.refresh_token import RefreshToken
from app.core.security import (
    hash_password, 
    verify_password,
    generate_refresh_token,
    hash_refresh_token
    )


def register_user(db: Session, email: str, password: str):
    result = db.execute(
        select(User).where(User.email == email)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise ValueError("Email already registered")

    hashed_password = hash_password(password)

    new_user = User(
        email=email,
        hashed_password=hashed_password
    )

    db.add(new_user)

    try:
        db.flush()
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already registered")

    return new_user

def authenticate_user(db: Session, email: str, password: str):
    result = db.execute(
            select(User).where(User.email == email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user is None:
        return None

    if not verify_password(password, existing_user.hashed_password):
        return None

    if not existing_user.is_active:
        return None

    return existing_user

def create_refresh_token(db:Session, user_id: int):
    raw_token = generate_refresh_token()
    token_hash = hash_refresh_token(raw_token)

    expires_at = datetime.now(timezone.utc) + timedelta(days=7)

    new_token = RefreshToken(
        user_id=user_id,
        token_hash=token_hash,
        expires_at=expires_at
    )
    db.add(new_token)
    db.flush()

    return raw_token
