import os
from dotenv import load_dotenv
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

load_dotenv()

class CommonSettings(BaseSettings):
    model_config = ConfigDict(
        extra='allow',
        env_file='.env'
        )

    TITLE: str = 'monitorline'
    VERSION: str = 'v1'
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    FERNET_KEY: str
    FASTAPI_HOST: str = os.getenv("FASTAPI_HOST", "127.0.0.1")
    FASTAPI_PORT: int = int(os.getenv("FASTAPI_PORT", 8000))
    SLACK_WEBHOOK_URL: str | None = None
    AIRFLOW_BASE_URL: str | None = None

class DevSettings(CommonSettings):
    """Local or Docker development settings."""
    DEBUG: bool = True
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://monitorline:monitorline@db:5432/monitorline"
    )
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379/0")
    UPSTASH_REDIS_REST_URL: str | None = None
    UPSTASH_REDIS_REST_TOKEN: str | None = None


class ProdSettings(CommonSettings):
    """Production settings (Aiven + Upstash)."""
    DEBUG: bool = False
    AIVEN_URL: str = os.getenv("AIVEN_URL")  # from Aiven
    UPSTASH_REDIS_REST_URL: str = os.getenv("UPSTASH_REDIS_REST_URL")
    UPSTASH_REDIS_REST_TOKEN: str = os.getenv("UPSTASH_REDIS_REST_TOKEN")


def get_settings():
    env = os.getenv("APP_ENV", "dev")
    if env == "prod":
        return ProdSettings()
    return DevSettings()


settings = get_settings()
