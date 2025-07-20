from src.core import ports
from src.core import domain
from typing import *
import logging

logger = logging.getLogger(__name__)

class IdentityService:
    def __init__(
            self,
            user_repository: ports.IUserRepository,
            cache_store: ports.ICacheStore,  # Empty cache store
            store: ports.IStore
        ):
        assert user_repository is not None, "Geocoder cannot be None"
        assert cache_store is not None, "Cache store cannot be None"
        assert store is not None, "Store cannot be None"
        
        self._user_respository = user_repository
        self._cache_store = cache_store
        self._store = store
    
    async def profile(self, user_id: int) -> domain.User:
        db = self._store.db()
        try:
            user = await self._cache_store.get_user(user_id)
            if not user:
                user = await self._user_respository.one(
                    db,
                    user_id
                )
                await self._cache_store.set_user(user)
            return user
        except Exception as e:
            logger.error(f"Error getting user {user_id}: {e}")
            raise e