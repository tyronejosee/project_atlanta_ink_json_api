"""Configs for Core Module."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # General Settings
    PROJECT_NAME: str = "Atlanta Ink API"
    API_V1_STR: str = "/api"

    # CORS Settings
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://atlanta-ink-studio.vercel.app",
    ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
