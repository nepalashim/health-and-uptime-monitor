import httpx
from app.config import settings


async def ping_url(url: str) -> dict:
    try:
        async with httpx.AsyncClient(timeout=settings.TIMEOUT) as client:
            response = await client.get(url)
            return {"status_code": response.status_code, "url": url}
    except Exception as e:
        return {"error": str(e), "url": url}
