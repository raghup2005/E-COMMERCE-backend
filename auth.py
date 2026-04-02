from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
from fastapi import FastAPI

app=FastAPI()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+(timedelta(minutes=30))
    to_encode.update(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def verify_token(token:str):
    try:
        payload=jwt.encode(token,SECRET_KEY,algorithm=ALGORITHM)
        return payload
    except JWTError:
        return None
