from pydantic import BaseModel, Field

__all__ = ["GeocodeResult"]

from typing import List, Optional
from pydantic import BaseModel


class AddressComponent(BaseModel):
    long_name: str
    short_name: str
    types: List[str]


class Viewport(BaseModel):
    northeast: dict[str, float]
    southwest: dict[str, float]


class Geometry(BaseModel):
    location: dict[str, float]
    location_type: str
    viewport: Viewport


class PlusCode(BaseModel):
    compound_code: str
    global_code: str


class GeocodeResult(BaseModel):
    address_components: List[AddressComponent]
    formatted_address: str
    geometry: Geometry
    place_id: str
    plus_code: Optional[PlusCode] = None
    types: List[str]


class GeocodeResponse(BaseModel):
    results: List[GeocodeResult]
    status: str


# Domain model for our application
class Geocode(BaseModel):
    latitude: float
    longitude: float
    formatted_address: str
    place_id: str