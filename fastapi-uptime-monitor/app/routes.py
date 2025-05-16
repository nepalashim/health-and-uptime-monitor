from datetime import datetime

from app.services.ping import ping_url
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "healthy"}


@router.get("/time")
def server_time():
    return {"time": datetime.utcnow().isoformat()}


@router.get("/ping")
async def ping_endpoint(url: str):
    result = await ping_url(url)
    return result
