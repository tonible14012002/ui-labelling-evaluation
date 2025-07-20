from pydantic_settings import BaseSettings

__all__ = ['settings']

class PostgresSettings(BaseSettings):
    PG_HOST: str = "localhost"
    PG_PORT: int = 5432
    PG_USER: str = "postgres"
    PG_PASSWORD: str = "devpassword"
    PG_DB: str = "postgres"
    PG_ASYNC_PREFIX: str = "postgresql+asyncpg"

class GoogleSettings(BaseSettings):
    GOOGLE_GEOCODE_API_KEY: str

class MainSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    API_SECRET_KEY: str

class RedisSettings(BaseSettings):
    REDIS_DSN: str = "redis://default:devpassword@localhost:6379/0"

class EnvironmentSettings(BaseSettings):
    ENV: str = "dev"

class Settings(
    PostgresSettings,
    GoogleSettings,
    MainSettings,
    RedisSettings,
    EnvironmentSettings,
    ):
    pass

settings = Settings(_env_file='.env', _env_file_encoding='utf-8')