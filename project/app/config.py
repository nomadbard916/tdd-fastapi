from functools import lru_cache
import logging
import os

from pydantic import BaseSettings, AnyUrl


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool | str = os.getenv("TESTING", False)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")  # type: ignore


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
