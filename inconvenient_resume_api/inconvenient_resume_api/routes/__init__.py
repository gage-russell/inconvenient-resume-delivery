from fastapi import APIRouter

from inconvenient_resume_api.routes import login, well_known, user

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(well_known.router, tags=["well-known"])
api_router.include_router(user.router, tags=["user"])
