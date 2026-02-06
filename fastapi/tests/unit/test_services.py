"""Service layer tests."""

from __future__ import annotations

import pytest

from project_name.schemas.item import ItemCreate
from project_name.schemas.user import UserCreate, UserUpdate
from project_name.services.item_service import ItemService
from project_name.services.user_service import UserService


@pytest.mark.asyncio
async def test_user_service_crud() -> None:
    service = UserService()

    users = await service.get_users()
    assert users

    created = await service.create_user(
        UserCreate(email="a@example.com", name="A", password="password123")
    )
    assert created.email == "a@example.com"

    existing = await service.get_user(1)
    assert existing is not None

    updated = await service.update_user(1, UserUpdate(name="B"))
    assert updated is not None
    assert updated.name == "B"

    deleted = await service.delete_user(1)
    assert deleted is True


@pytest.mark.asyncio
async def test_item_service_crud() -> None:
    service = ItemService()

    items = await service.list_items()
    assert items

    created = await service.create_item(ItemCreate(name="Item", description=None))
    assert created.name == "Item"
