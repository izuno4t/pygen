"""Dependency tests."""

from __future__ import annotations

import pytest
from fastapi import HTTPException

from project_name.dependencies import get_current_user


def test_get_current_user_requires_header() -> None:
    with pytest.raises(HTTPException):
        get_current_user(authorization=None)


def test_get_current_user_returns_user() -> None:
    result = get_current_user(authorization="Bearer token")
    assert result["user_id"] == 1
