from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "UptimeMonitor"
    TIMEOUT: int = 5

    class Config:
        env_file = ".env"


settings = Settings()
