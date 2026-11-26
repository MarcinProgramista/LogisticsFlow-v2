import jwt
from app.core.jwt import create_access_token, SECRET_KEY, ALGORITHM, verify_access_token
from datetime import datetime, timezone, timedelta

def test_create_access_token():
    token = create_access_token(user_id=1)

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    expire = datetime.fromtimestamp(payload["exp"], tz=timezone.utc)

    now = datetime.now(timezone.utc)
    assert timedelta(minutes=14,seconds=59) < expire - now <= timedelta(minutes=15)
    assert payload["sub"] == "1"
    assert "exp" in payload

def test_verify_valid_access_token():
    token = create_access_token(user_id=1)

    payload = verify_access_token(token)
    assert payload is not None
    assert payload["sub"] == "1"

def test_verify_invalid_access_token():
    payload = verify_access_token("invalid.token.value")

    assert payload is None

def test_verify_expired_access_token():
    expired_token = jwt.encode(
        {
            "sub": "1",
            "exp": datetime.now(timezone.utc) - timedelta(minutes=1)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )