from src.core import ports
from src.core import domain
from typing import Optional, List
from pydantic import RootModel, TypeAdapter
import logging
import json

logger = logging.getLogger(__name__)

class CacheStore(ports.ICacheStore):
    def __init__(self, cache: ports.ICache):
        self._cache = cache
    
    def _make_geocode_key(self, address: str) -> str:
        # Create a unique key for the geocode based on the address
        return f"geocode:address:v1:{address}"

    async def get_geocode(self, address: str) -> Optional[List[domain.GeocodeResult]]:
        try:
            # Attempt to retrieve the geocode from the cache
            cached_geocodes = await self._cache.get(self._make_geocode_key(address))
            if cached_geocodes:
                # If found, deserialize the cached )geocode
                return TypeAdapter(List[domain.GeocodeResult]).validate_json(cached_geocodes)
            else:
                logger.debug(f"No geocode found in cache for address: {address}")
                return None
        except Exception as e:
            logger.error(f"Error retrieving geocode from cache: {e}")
            return None

    async def set_geocode(self, address: str, geocodes: List[domain.GeocodeResult]):
        class GeocodeResultList(RootModel):
            root: List[domain.GeocodeResult]
        jsonstr = GeocodeResultList(root=geocodes).model_dump_json()
        try:
            # Serialize the geocode and store it in the cache
            await self._cache.set(self._make_geocode_key(address), jsonstr, expire=3600000) # 1 hour
        except Exception as e:
            logger.error(f"Error setting geocode in cache: {e}")
    
    async def get_user(self, user_id):
        return None
        pass
    
    async def set_user(self, user):
        pass