"""API client."""

from __future__ import annotations

import httpx


def fetch_status(endpoint: str) -> dict:
    response = httpx.get(endpoint, timeout=10)
    response.raise_for_status()
    return response.json()
