import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PG_URL: str
    REDIS_URL: str
    TEST_PG_URL: str
    TEST_REDIS_URL: str
    ENV_FILE: str
    ENV: str

    if os.path.exists(".env"):
        ENV_FILE = ".env"
    else:
        ENV_FILE = "../.env"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra="ignore",
    )


Config = Settings()
