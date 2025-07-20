from src.core import ports
from src.core import domain
from typing import *
import logging

logger = logging.getLogger(__name__)

class GeocodeService:
    def __init__(
            self,
            geocoder: ports.IGeocode,
            cache_store: ports.ICacheStore,
        ):
        assert geocoder is not None, "Geocoder cannot be None"
        assert cache_store is not None, "Cache store cannot be None"
        
        self._geocoder = geocoder
        self._cache_store = cache_store
 
    async def get_locations(self, address) -> List[domain.GeocodeResult]:
        try:
            locations = await self._cache_store.get_geocode(address)
            if not locations:

                logger.info(f"Cache miss for address: {address}")

                locations = await self._geocoder.geocode(address)
                await self._cache_store.set_geocode(address, locations)

            return locations
        except Exception as e:
            logger.error(f"Error geocoding address {address}: {e}")
            raise e