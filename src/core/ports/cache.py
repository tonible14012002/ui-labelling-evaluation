from abc import ABC, abstractmethod
from typing import Optional, List
from src.core import domain

__all__ = [
    "ICache",
    "ICacheStore",
]

class ICache(ABC):
    """
    Interface for cache operations.
    """
    @abstractmethod
    async def set(
        self,
        key: str,
        value: str,
        expire: Optional[int] = None, # Miliseconds,
        not_existed_only: Optional[bool] = False,
        existed_only: Optional[bool] = False,
        expire_time_stamp: Optional[int] = None, # Miliseconds
        keep_ttl: Optional[bool] = False, # Keep the time to live of the key
    ):
        """
        Set a value in the cache with an optional expiration time.
        """

    @abstractmethod
    async def get(self, key: str) -> Optional[str]:
        """
        Get a value from the cache.
        """
    
    @abstractmethod
    async def delete(self, *keys: str):
        """
        Delete a key from the cache.
        """
    
    @abstractmethod
    async def expire(
        self,
        key: str,
        expire: int,
        not_existed_only: Optional[bool] = False,
        existed_only: Optional[bool] = False,
        gt_only: Optional[bool] = False, # greated than exited expiration only
        lt_only: Optional[bool] = None, # less than expiration time
    ) -> bool:
        """
        Set the expiration time for a key in seconds.
        """
        pass
    
    @abstractmethod
    async def close(self) -> None:
        """
        Close the cache connection.
        """

class ICacheStore(ABC):
    """
    Interface cache store.
    """

    # Geocode Services
    @abstractmethod
    def get_geocode(self, address: str) -> Optional[List[domain.GeocodeResult]]:
        """
        Get the geocode for a given address.
        """

    @abstractmethod
    def set_geocode(self, address: str, geocode: List[domain.GeocodeResult]) -> None:
        """
        Set the geocode for a given address.
        """
    
    # User
    @abstractmethod
    def set_user(self, user: domain.User) -> None:
        """
        Set the user in the cache.
        """
    
    @abstractmethod
    def get_user(self, user_id: int) -> Optional[domain.User]:
        """
        Get the user from the cache.
        """
    