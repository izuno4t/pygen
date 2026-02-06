"""User service."""

from __future__ import annotations

from datetime import datetime

from project_name.schemas.user import UserCreate, UserRead, UserUpdate


class UserService:
    async def get_users(self, skip: int = 0, limit: int = 100) -> list[UserRead]:
        now = datetime.utcnow()
        return [
            UserRead(
                id=1,
                email="user@example.com",
                name="Example",
                is_active=True,
                created_at=now,
                updated_at=now,
            )
        ]

    async def create_user(self, user_in: UserCreate) -> UserRead:
        now = datetime.utcnow()
        return UserRead(
            id=1,
            email=user_in.email,
            name=user_in.name,
            is_active=user_in.is_active,
            created_at=now,
            updated_at=now,
        )

    async def get_user(self, user_id: int) -> UserRead | None:
        if user_id != 1:
            return None
        now = datetime.utcnow()
        return UserRead(
            id=1,
            email="user@example.com",
            name="Example",
            is_active=True,
            created_at=now,
            updated_at=now,
        )

    async def update_user(self, user_id: int, user_in: UserUpdate) -> UserRead | None:
        if user_id != 1:
            return None
        now = datetime.utcnow()
        return UserRead(
            id=1,
            email=user_in.email or "user@example.com",
            name=user_in.name or "Example",
            is_active=user_in.is_active if user_in.is_active is not None else True,
            created_at=now,
            updated_at=now,
        )

    async def delete_user(self, user_id: int) -> bool:
        return user_id == 1
