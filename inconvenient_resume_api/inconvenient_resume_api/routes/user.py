from fastapi import APIRouter, Response

from inconvenient_resume_api.deps import CurrentUser, SessionDep
from inconvenient_resume_api.logic.user.queries.get_resume_query import GetResumeQuery, GetResumeQueryHandler
from inconvenient_resume_api.models import UserPublic

router = APIRouter()


@router.get("/user/me", response_model=UserPublic)
def read_user_me(current_user: CurrentUser) -> UserPublic:
    """
    Get current user.
    """
    return current_user

@router.get("/user/resume", response_model=UserPublic)
def read_user_me(session: SessionDep, current_user: CurrentUser) -> UserPublic:
    """
    Get current user.
    """
    query = GetResumeQuery(user=current_user)
    resume = GetResumeQueryHandler(session).handle(query)
    # TODO: close buffer with background task
    headers = {'Content-Disposition': 'inline; filename="gage_russell_resume.pdf"'}
    return Response(content=resume.getvalue(), media_type="application/pdf", headers=headers)
