from app.core.security import hash_password,verify_password

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

