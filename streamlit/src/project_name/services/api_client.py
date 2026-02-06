"""API client."""

from __future__ import annotations

from typing import Any

import httpx


def fetch_status(endpoint: str) -> dict[str, Any]:
    response = httpx.get(endpoint, timeout=10)
    response.raise_for_status()
    data: dict[str, Any] = response.json()
    return data
