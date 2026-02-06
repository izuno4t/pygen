"""Item endpoints tests."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from fastapi.testclient import TestClient


def test_list_items(client: TestClient) -> None:
    response = client.get("/api/v1/items/")
    assert response.status_code == 200


def test_create_item(client: TestClient) -> None:
    payload = {"name": "Item", "description": None}
    response = client.post("/api/v1/items/", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Item"
