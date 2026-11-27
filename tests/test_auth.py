from sqlalchemy import select
from app.models.refresh_token import RefreshToken
from app.core.security import hash_refresh_token

def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "newuser@example.com",
            "password": "Test123456!"
        }
    )

    assert response.status_code == 201
    assert response.json()["email"] == "newuser@example.com"
    assert "password" not in response.json()
    assert "hashed_password" not in response.json()

def test_register_user_duplicate_email(client):
    user_data = {
        "email": "duplicate@example.com",
        "password": "Test123456!"
    }

    first_response = client.post("/auth/register", json=user_data)
    second_response = client.post("/auth/register", json=user_data)

    assert first_response.status_code == 201
    assert second_response.status_code == 400

def test_register_user_password_too_short(client):
    response = client.post(
        "/auth/register",
        json = {
            "email": "shortpass@example.com",
            "password": "123"
        }
    )

    assert response.status_code == 422

def test_login_user(client, db_session):
    register_response = client.post(
        "/auth/register",
        json = {
            "email": "login@example.com",
            "password": "Test123456!"
        }
    )
    user_id = register_response.json()["id"]

    response = client.post(
        "/auth/login",
        json = {
            "email": "login@example.com",
            "password": "Test123456!"
        }
    )

    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["user"]["email"] == "login@example.com"
    assert "id" in response.json()["user"]
    assert response.json()["refresh_token"]
    assert response.json()["token_type"] == "bearer"

    result = db_session.execute(
        select(RefreshToken).where(
            RefreshToken.user_id == user_id
        )
    )
    saved_token = result.scalar_one_or_none()

    assert saved_token is not None
    assert saved_token.token_hash == hash_refresh_token(
        response.json()["refresh_token"]
    )
    assert saved_token.token_hash != response.json()["refresh_token"]

def test_login_user_wrong_password(client):
    client.post(
        "/auth/register",
        json={
            "email": "wrongpass@example.com",
            "password": "Test123456!"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "wrongpass@example.com",
            "password":"worngPassword123!"
       }
    )

    assert response.status_code == 401
