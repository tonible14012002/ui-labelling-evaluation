from abc import ABC, abstractmethod
from typing import *
from .. import domain


class IGeocode(ABC):
    """
    GeocodePort is an interface for external geocoding service.
    """
    
    @abstractmethod
    async def geocode(self, address: str) -> List[domain.GeocodeResult]:
        """
        Geocode an address to get its latitude and longitude.

        :param address: The address to geocode.
        :return: A dictionary containing the latitude and longitude of the address.
        """
        pass