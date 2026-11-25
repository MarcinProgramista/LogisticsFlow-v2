from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.core.security import hash_password, verify_password


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
