"""Health check endpoints."""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    version: str


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="healthy", version="0.1.0")


@router.get("/ready")
async def readiness_check() -> dict[str, str]:
    return {"status": "ready"}
