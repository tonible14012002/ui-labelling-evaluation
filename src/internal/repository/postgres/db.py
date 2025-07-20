from src.core import ports

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import settings
from typing import AsyncGenerator

def create_pg_async_engine() -> AsyncEngine:
    """
    Get the PostgreSQL URI from the settings.
    """
    PG_URI = f"{settings.PG_USER}:{settings.PG_PASSWORD}@{settings.PG_HOST}:{settings.PG_PORT}/{settings.PG_DB}"
    DB_URL = f"{settings.PG_ASYNC_PREFIX}://{PG_URI}"
    async_engine = create_async_engine(DB_URL, echo=settings.ENV=="dev", future=True)
    return async_engine


class PostgresStore(ports.IStore):
    def __init__(self, engine: AsyncEngine):
        self._async_engine = engine
        self._session_maker = sessionmaker(
            bind=self._async_engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
        
    async def db(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session_maker() as session:
            yield session