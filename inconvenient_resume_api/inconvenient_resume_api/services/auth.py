from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from passlib.context import CryptContext

from inconvenient_resume_api.config import settings


class AuthService:
    ALGORITHM = "HS256"
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode = {"exp": expire, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=AuthService.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return AuthService.PWD_CONTEXT.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return AuthService.PWD_CONTEXT.hash(password)
    
    @staticmethod
    def get_expires_delta() -> timedelta:
        return timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
