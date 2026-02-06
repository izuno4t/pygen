"""User endpoints."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from project_name.schemas.user import UserCreate, UserRead, UserUpdate
from project_name.services.user_service import UserService


router = APIRouter()


def get_user_service() -> UserService:
    return UserService()


UserServiceDep = Annotated[UserService, Depends(get_user_service)]


@router.get("/", response_model=list[UserRead])
async def list_users(
    service: UserServiceDep,
    skip: int = 0,
    limit: int = 100,
) -> list[UserRead]:
    return await service.get_users(skip=skip, limit=limit)


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    service: UserServiceDep,
) -> UserRead:
    return await service.create_user(user_in)


@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: int,
    service: UserServiceDep,
) -> UserRead:
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.patch("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: int,
    user_in: UserUpdate,
    service: UserServiceDep,
) -> UserRead:
    user = await service.update_user(user_id, user_in)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    service: UserServiceDep,
) -> None:
    deleted = await service.delete_user(user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
