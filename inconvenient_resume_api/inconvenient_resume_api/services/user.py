import importlib.resources
from io import BytesIO
import importlib
from sqlmodel import Session, select

from inconvenient_resume_api.models import User, UserCreate
from inconvenient_resume_api.services.auth import AuthService
from inconvenient_resume_api import assets


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        user = self.session.exec(statement).first()
        return user

    def authenticate_user(self, email: str, password: str) -> User | None:
        user = self.get_user_by_email(email)
        if not user:
            return None
        if not user.is_active:
            return None
        if not AuthService.verify_password(password, user.hashed_password):
            return None
        return user
    
    def create_user(self, user_create: UserCreate) -> User:
        user = User.model_validate(
            user_create, update={"hashed_password": AuthService.get_password_hash(user_create.password)}
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def get_resume(self) -> BytesIO:
        # use importlib to load pdf from project root / assets / gage_russell_resume.pdf
        with importlib.resources.open_binary(assets, "gage_russell_resume.pdf") as f:
            return BytesIO(f.read())
