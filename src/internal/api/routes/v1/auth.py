from src.core import domain
from src.internal.api.routes.base import BaseAPIRouter
from typing import *

class AuthAPIRouter(BaseAPIRouter):
    pass

router = AuthAPIRouter(
    tags=["v1/auth-service"],
)

@router.get(
    "/me",
    status_code=200,
    response_model=domain.User,
)
async def me():
    # Get the geocode from the cache
    return await router.entities.identity_service.profile(1)
