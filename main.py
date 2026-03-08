from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from app.api.v1.user_routes import user_router
from app.config.settings import BaseAppSettings, get_config

test_route = APIRouter(prefix="/test", tags=["test"])

routes = [test_route, user_router]


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncIterator[None]:
    """Lifespan."""
    for route in routes:
        application.include_router(
            route,
            prefix=settings.api_prefix,
        )
    yield


settings: BaseAppSettings = get_config()


app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url=f"{settings.api_prefix}/docs",
    lifespan=lifespan,
)


@app.get("/")
def read_root() -> dict[str, str]:
    """Root endpoint."""
    return {"Hello": "World"}


@test_route.get("")
def test() -> str:
    """Test endpoint."""
    return settings.sqlmodel_database_uri
