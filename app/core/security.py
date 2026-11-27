from pwdlib import PasswordHash
import secrets
import hashlib

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    
    return password_hash.hash(password)

def verify_password(password:str, hashed_password:str) -> bool:
    return password_hash.verify(password,hashed_password)

def generate_refresh_token() -> str:
    return secrets.token_urlsafe(54)

def hash_refresh_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()

