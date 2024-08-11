from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from inconvenient_resume_api.deps import SessionDep
from inconvenient_resume_api.logic.user.commands.login_command import LoginCommand, LoginCommandHandler
from inconvenient_resume_api.models import Token


router = APIRouter()


@router.post("/login/access-token")
def login_access_token(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    access_token = LoginCommandHandler(session).handle(LoginCommand(form_data=form_data))
    return Token(access_token=access_token)
