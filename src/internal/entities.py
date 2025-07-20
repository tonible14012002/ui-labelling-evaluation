from dataclasses import dataclass
from src.core import services
from fastapi import FastAPI

@dataclass
class Entities:
    """
    Class holding the entities of the application.
    """
    geocode_service: services.GeocodeService
    identity_service: services.IdentityService