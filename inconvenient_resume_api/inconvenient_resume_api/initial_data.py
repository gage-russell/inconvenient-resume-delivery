import logging

from inconvenient_resume_api.models import UserCreate
from inconvenient_resume_api.services.user import UserService
from sqlmodel import Session, create_engine

from inconvenient_resume_api.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Creating initial data")
    engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
    with Session(engine) as session:
        user_service = UserService(session)
        user = user_service.get_user_by_email(email=settings.FIRST_SUPERUSER)
        if not user:
            user_service.create_user(
                user_create=UserCreate(
                    email=settings.FIRST_SUPERUSER,
                    password=settings.FIRST_SUPERUSER_PASSWORD,
                    is_superuser=True,
                )
            )
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
