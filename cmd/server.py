import contextlib
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError

from src.internal.api.exceptions import (
    http_exception_handler,
    unhandled_exception_handler,
    request_validation_exception_handler
)
from src.internal.repository import postgres
from src.internal.cache import redis
from src.internal.cache import store as cache_store
from src.internal.geocode import google_geocode
from src.internal.entities import Entities
from src.internal.api.routes import v1 as v1_routes

from src.core import services
from src.config import settings

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    print("Shutting down app.")

app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)

# Initialize services

engine = postgres.create_pg_async_engine()
store = postgres.PostgresStore(engine=engine)

redis_cache = redis.RedisCache.initialize(settings.REDIS_DSN)
cache_store = cache_store.CacheStore(cache=redis_cache)

google_geocode = google_geocode.GoogleGeocoder(
    api_key=settings.GOOGLE_GEOCODE_API_KEY
)

user_repository = postgres.UserRepository()

geocode_service = services.GeocodeService(
    geocoder=google_geocode,
    cache_store=cache_store
)

identity_servce = services.IdentityService(
    cache_store=cache_store,
    store=store,
    user_repository=user_repository
)

entities = Entities(
    geocode_service=geocode_service,
    identity_service=identity_servce
)

# Bind entities to handlers
v1_routes.geocode.router.set_entities(entities),
v1_routes.auth.router.set_entities(entities),

# Bind routes
app.include_router(
    v1_routes.geocode.router,
    prefix="/api/v1/geocode",
)
app.include_router(
    v1_routes.auth.router,
    prefix="/api/v1/auth",
)

@app.get("/")
async def root():
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run("server:app", host=settings.HOST, port=settings.PORT, reload=True)