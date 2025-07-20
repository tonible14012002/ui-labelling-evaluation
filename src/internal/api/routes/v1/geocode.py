from src.core import domain
from src.internal.api.routes.base import BaseAPIRouter
from typing import List

class GeocodeAPIRouter(BaseAPIRouter):
    pass

router = GeocodeAPIRouter(
    tags=["v1/geocode"],
)

@router.get(
    "/search",
    status_code=200,
    response_model=List[domain.GeocodeResult],
)
async def geocode(
    address: str,
):
    """
    Geocode an address.
    """
    # Get the geocode from the cache
    location = await router.entities.geocode_service.get_locations(address=address)
    return location