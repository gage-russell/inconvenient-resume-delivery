from dataclasses import dataclass

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from inconvenient_resume_api.services.auth import AuthService
from inconvenient_resume_api.services.user import UserService

@dataclass
class LoginCommand:
    form_data: OAuth2PasswordRequestForm

class LoginCommandHandler:

    def __init__(self, session):
        self.session = session
        self.user_service = UserService(session)

    def handle(self, command: LoginCommand):
        user = self.user_service.authenticate_user(
            command.form_data.username, command.form_data.password
        )
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        elif not user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user")
        access_token_expires = AuthService.get_expires_delta()
        return AuthService.create_access_token(user.id, expires_delta=access_token_expires)
