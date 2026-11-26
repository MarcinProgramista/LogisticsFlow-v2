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
