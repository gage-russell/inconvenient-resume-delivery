from dataclasses import dataclass
from io import BytesIO

from inconvenient_resume_api.models import User
from inconvenient_resume_api.services.user import UserService

@dataclass
class GetResumeQuery:
    # TODO: could support resumes for different users, but just playing around
    user: User

class GetResumeQueryHandler:

    def __init__(self, session):
        self.session = session
        self.user_service = UserService(session)

    def handle(self, query: GetResumeQuery) -> BytesIO:
        return self.user_service.get_resume()
