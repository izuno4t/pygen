from __future__ import annotations

from fastapi import FastAPI

from project_name.core.config import get_settings
from project_name.routers import health, items, users


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version=settings.app_version)
    app.include_router(health.router, tags=["health"])
    app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
    app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
    return app


app = create_app()
