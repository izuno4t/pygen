"""Item service."""

from __future__ import annotations

from project_name.schemas.item import ItemCreate, ItemRead


class ItemService:
    async def list_items(self) -> list[ItemRead]:
        return [ItemRead(id=1, name="Sample", description=None)]

    async def create_item(self, item_in: ItemCreate) -> ItemRead:
        return ItemRead(id=1, name=item_in.name, description=item_in.description)
