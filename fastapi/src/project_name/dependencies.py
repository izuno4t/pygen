"""Common dependencies."""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import Depends, Header, HTTPException, status

from project_name.core.config import Settings, get_settings


SettingsDep = Annotated[Settings, Depends(get_settings)]


class PaginationParams:
    def __init__(self, skip: int = 0, limit: int = 100) -> None:
        self.skip = skip
        self.limit = min(limit, 1000)


PaginationDep = Annotated[PaginationParams, Depends()]


def get_current_user(
    authorization: Annotated[str | None, Header()] = None,
    settings: SettingsDep | None = None,
) -> dict[str, Any]:
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header required",
        )
    _ = settings
    return {"user_id": 1, "email": "user@example.com"}


CurrentUserDep = Annotated[dict[str, Any], Depends(get_current_user)]
