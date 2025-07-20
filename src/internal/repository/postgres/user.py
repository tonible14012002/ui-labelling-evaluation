from sqlalchemy.ext.asyncio import AsyncSession
from src.core import ports
from src.core import domain
from typing import *

class UserRepository(ports.IUserRepository):
    async def one(self, db: AsyncSession, user_id: int) -> domain.User:
        print("\n", db, "\n")
        return domain.User(
            id=user_id,
            name="John Doe",
            email="hello_world@gmail.com",
            created_at="2023-01-01T00:00:00Z",
            updated_at="2023-01-01T00:00:00Z",
            activated_at="2023-01-01T00:00:00Z",
        )
    
    async def update(self, db: AsyncSession, user_id: int, user_data: dict) -> Optional[domain.User]:
        return None

    async def list(self, db: AsyncSession, q: domain.UserQuery) -> List[domain.User]:
        return []