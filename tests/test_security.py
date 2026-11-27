from app.core.security import (
    hash_password,
    verify_password,
    generate_refresh_token,
    hash_refresh_token
    )

def test_hash_password():
    password = "Test12345"

    hashed = hash_password(password)

    assert hashed != password

def test_hash_password_correct():
    password = "Test12345"
    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password)

def test_hash_password_incorrect():
    password = "Test12345"
    hashed_password = hash_password(password)

    assert verify_password("WrongPassword", hashed_password) is not True

def test_generate_refresh_token():
    token = generate_refresh_token()

    assert isinstance(token, str)
    assert len(token) > 0

def test_generate_refresh_token_unique():
    token1 = generate_refresh_token()
    token2 = generate_refresh_token()

    assert token1 != token2 

def test_hash_refresh_token():
    token = generate_refresh_token()

    hashed = hash_refresh_token(token)

    assert len(hashed) == 64
    assert hashed != token

def test_hash_refresh_token_is_deterministic():
    token = generate_refresh_token()

    hash1 = hash_refresh_token(token)
    hash2 = hash_refresh_token(token)

    assert hash1 == hash2 

