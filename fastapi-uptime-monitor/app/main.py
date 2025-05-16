from app.config import settings
from app.routes import router
from fastapi import FastAPI

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Uptime Monitor"}
