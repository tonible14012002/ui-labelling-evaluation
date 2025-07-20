from fastapi import APIRouter
from fastapi.requests import Request
from src.internal.entities import Entities

class BaseAPIRouter(APIRouter):
    entities: Entities
    """
    Inherit this class for accessing entities.
    """
    
    def set_entities(self, entities: Entities) -> None:
        """
        Set entities to the app instance.
        """
        self.entities = entities