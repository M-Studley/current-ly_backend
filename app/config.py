from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PG_URL: str
    REDIS_URL: str

    model_config = SettingsConfigDict(
        # Running from Pycharm
        env_file="../.env",
        # Running alembic commands
        # env_file=".env",
        extra="ignore",
    )


Config = Settings()
