"""Integration smoke tests."""

from __future__ import annotations

from project_name import app as app_module


def test_app_importable() -> None:
    assert app_module is not None
