from src.core import ports
from typing import Optional, Any
from redis.asyncio import Redis, ConnectionPool

class RedisCache(ports.ICache):
    """
    Singleton class for Redis cache.
    """
    _instance: Optional["RedisCache"] = None
    pool: Optional[ConnectionPool] = None
    client: Optional[Redis] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Factory
    @classmethod
    def initialize(cls, redis_url: str) -> None:
        instance = cls()
        if instance.pool is None:
            instance.pool = ConnectionPool.from_url(redis_url)
            instance.client = Redis(connection_pool=instance.pool)
        return instance
    
    async def close(self) -> None:
        return await self.client.aclose()
    
    # Mutators
    async def set(
        self,
        key: str,
        value: str,
        expire: Optional[int] = None, # Miliseconds,
        not_existed_only: Optional[bool] = False,
        existed_only: Optional[bool] = False,
        expire_time_stamp: Optional[int] = None, # Miliseconds
        keep_ttl: Optional[bool] = False, # Keep the time to live of the key
    ) -> bool:
        await self.client.set(
            key,
            value.encode("utf-8"),
            ex=expire,
            nx=not_existed_only,
            xx=existed_only,
            exat=expire_time_stamp,
            keepttl=keep_ttl,
        )
        
    async def get(self, key: str) -> str:
        val = await self.client.get(key)
        return val.decode("utf-8") if val else None
    
    async def delete(self, *key: str) -> bool:
        return await self.client.delete(*key)
    
    async def expire(
        self,
        key: str,
        expire: int,
        not_existed_only: Optional[bool] = False,
        existed_only: Optional[bool] = False,
        gt_only: Optional[bool] = False,
        lt_only: Optional[bool] = None,
    ) -> bool:
        return await self.client.expire(
            key,
            expire,
            nx=not_existed_only,
            xx=existed_only,
            gt=gt_only,
            lt=lt_only
        )