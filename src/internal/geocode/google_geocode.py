from pydantic import TypeAdapter    
import httpx
from src.core import domain
from typing import *

from src.core import ports
from src.core import domain

class GoogleGeocoder(ports.IGeocode):
    def __init__(self, api_key: str):
        self._key = api_key

    async def geocode(self, address: str) -> List[domain.GeocodeResult]:
        async with httpx.AsyncClient() as client:
            await client.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&sensor=false&key={self._key}")
            resp = {
                "results": [
                    {
                        "address_components": [
                            {
                                "long_name": "1600",
                                "short_name": "1600",
                                "types": [
                                    "street_number"
                                ]
                            },
                            {
                                "long_name": "Amphitheatre Parkway",
                                "short_name": "Amphitheatre Pkwy",
                                "types": [
                                    "route"
                                ]
                            },
                            {
                                "long_name": "Mountain View",
                                "short_name": "Mountain View",
                                "types": [
                                    "locality",
                                    "political"
                                ]
                            },
                            {
                                "long_name": "Santa Clara County",
                                "short_name": "Santa Clara County",
                                "types": [
                                    "administrative_area_level_2",
                                    "political"
                                ]
                            },
                            {
                                "long_name": "California",
                                "short_name": "CA",
                                "types": [
                                    "administrative_area_level_1",
                                    "political"
                                ]
                            },
                            {
                                "long_name": "United States",
                                "short_name": "US",
                                "types": [
                                    "country",
                                    "political"
                                ]
                            },
                            {
                                "long_name": "94043",
                                "short_name": "94043",
                                "types": [
                                    "postal_code"
                                ]
                            },
                            {
                                "long_name": "1351",
                                "short_name": "1351",
                                "types": [
                                    "postal_code_suffix"
                                ]
                            }
                        ],
                        "formatted_address": "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA",
                        "geometry": {
                            "location": {
                                "lat": 37.4222804,
                                "lng": -122.0843428
                            },
                            "location_type": "ROOFTOP",
                            "viewport": {
                                "northeast": {
                                    "lat": 37.4237349802915,
                                    "lng": -122.083183169709
                                },
                                "southwest": {
                                    "lat": 37.4210370197085,
                                    "lng": -122.085881130292
                                }
                            }
                        },
                        "place_id": "ChIJRxcAvRO7j4AR6hm6tys8yA8",
                        "plus_code": {
                            "compound_code": "CWC8+W7 Mountain View, CA",
                            "global_code": "849VCWC8+W7"
                        },
                        "types": [
                            "street_address"
                        ]
                    }
                ],
                "status": "OK"
            }
            ok = resp["status"] == "OK"
            if not ok:
                raise domain.GoogleGeocodeException("Google geocode api status not OK")

        return TypeAdapter(List[domain.GeocodeResult]).validate_python(resp["results"])