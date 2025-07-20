from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from src.core import domain
from typing import List

class IStore(ABC):
    @abstractmethod
    def db() -> AsyncSession:
        pass

class IUserRepository(ABC):
    @abstractmethod
    def one(self, db: AsyncSession, user_id: int) -> domain.User:
        pass

    @abstractmethod
    def update(self, db: AsyncSession, user_id: int, user_data: dict) -> domain.User:
        pass

    @abstractmethod
    def list(self, db: AsyncSession, q: domain.UserQuery) -> List[domain.User]:
        pass