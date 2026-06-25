from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    gemini_api_key: str
    gemini_model: str = "gemini-2.5-flash"
    log_level: str = "INFO"
    app_name: str = "Text Tools API"


@lru_cache
def get_settings() -> Settings:
    # cached so we don't re-read the .env on every request
    return Settings()
