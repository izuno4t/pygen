"""User endpoints tests."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from fastapi.testclient import TestClient


def test_list_users(client: TestClient) -> None:
    response = client.get("/api/v1/users/")
    assert response.status_code == 200


def test_create_user(client: TestClient) -> None:
    payload = {"email": "test@example.com", "name": "Test", "password": "password123"}
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
