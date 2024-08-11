from typing import Annotated

from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/.well-known/health")
def well_known_health() -> Annotated[dict, Depends()]:
    """
    Health check endpoint
    """
    return {"status": "ok"}
