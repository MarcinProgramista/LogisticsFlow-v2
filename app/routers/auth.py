from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin, TokenResponse
from app.services.user_service import (
        register_user,
        authenticate_user,
        create_refresh_token
    )
from app.core.jwt import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", response_model=UserResponse, status_code=201)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
): 
    try:
        new_user = register_user(
            db=db,
            email=user_data.email,
            password=user_data.password
        )

        db.commit()
    except ValueError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return new_user

@router.post("/login", response_model=TokenResponse)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
): 
    user = authenticate_user(
        db=db,
        email=user_data.email,
        password=user_data.password
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(
        db=db,
        user_id=user.id
    )
    db.commit()
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email
        }
    }
