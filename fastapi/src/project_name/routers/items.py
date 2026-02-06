"""Item endpoints."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, status

from project_name.schemas.item import ItemCreate, ItemRead
from project_name.services.item_service import ItemService

router = APIRouter()


def get_item_service() -> ItemService:
    return ItemService()


ItemServiceDep = Annotated[ItemService, Depends(get_item_service)]


@router.get("/", response_model=list[ItemRead])
async def list_items(service: ItemServiceDep) -> list[ItemRead]:
    return await service.list_items()


@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
async def create_item(item_in: ItemCreate, service: ItemServiceDep) -> ItemRead:
    return await service.create_item(item_in)
