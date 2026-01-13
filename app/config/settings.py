from __future__ import annotations

import os
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseAppSettings(BaseSettings):
    """Base application settings."""

    RUN_MODE: Literal["development", "production"] = Field(default="development")
    PROJECT_NAME: str
    SECRET_KEY: str = Field(..., min_length=16)
    URL_PROTOCOL: str = Field(default="http://")
    URL_BASE: str
    API_VERSION: str = Field(default="/api/v1")
    SERV_URL: str
    VERSION: str

    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: str

    # 60 minutes * 24 hours = 1 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    @property
    def api_prefix(self) -> str:
        """Prefix that combines microservice name and API version."""
        return f"{self.SERV_URL.rstrip('/')}{self.API_VERSION}"

    @property
    def sqlmodel_database_uri(self) -> str:
        """Constucts the SQLAlchemy database URI."""
        return (
            f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
        )


class DevelopmentSettings(BaseAppSettings):
    """Configurations settings Development environment."""

    model_config = SettingsConfigDict(env_file="docker/dev/.env", extra="ignore")
    DEBUG: bool = True
    TESTING: bool = False


APP_SETTINGS = {"development": DevelopmentSettings}


def get_config() -> DevelopmentSettings:
    """Return the configuration depending on the execution environment (production or development)."""
    mode = os.getenv("RUN_MODE", "development").lower()
    return APP_SETTINGS[mode]()
