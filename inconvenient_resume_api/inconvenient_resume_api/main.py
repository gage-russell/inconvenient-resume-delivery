from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
from alembic.config import Config
from alembic import command
import logging
from pathlib import Path

from inconvenient_resume_api.routes import api_router
from inconvenient_resume_api.config import settings
from inconvenient_resume_api import initial_data

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"

# hack to avoid init containers and jobs -- trying to throw something together in a couple hours :)
def run_migrations(script_location: str, dsn: str) -> None:
    logger.info('Running DB migrations in %r on %r', script_location, dsn)
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', script_location)
    alembic_cfg.set_main_option('sqlalchemy.url', dsn)
    command.upgrade(alembic_cfg, 'head')

project_path = Path(__file__).parents[1]
script_location = project_path / "alembic"
dsn = settings.SQLALCHEMY_DATABASE_URI

# TODO: create init container and remove this from the main app
run_migrations(str(script_location), str(dsn))
initial_data.main()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
