"""Utility helper tests."""

from __future__ import annotations

from project_name.utils import add


def test_add() -> None:
    assert add(1, 2) == 3
