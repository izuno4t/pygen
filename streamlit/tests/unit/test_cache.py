"""Cache helper tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx
import streamlit as st

from project_name.utils import cache


if TYPE_CHECKING:
    from pathlib import Path

    import pytest


def test_load_data(tmp_path: Path) -> None:
    csv_path = tmp_path / "data.csv"
    csv_path.write_text("date,value\n2024-01-01,1\n")

    data = cache.load_data(str(csv_path))
    assert len(data) == 1


def test_fetch_api_data(monkeypatch: pytest.MonkeyPatch) -> None:
    class DummyResponse:
        def json(self):
            return {"ok": True}

    def dummy_get(_endpoint):
        return DummyResponse()

    monkeypatch.setattr(httpx, "get", dummy_get)
    result = cache.fetch_api_data("https://example.com")
    assert result["ok"] is True


def test_get_database_connection(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(st, "secrets", {"database": {"connection_string": "db"}})

    class DummyEngine:
        pass

    def dummy_create_engine(_conn):
        return DummyEngine()

    monkeypatch.setattr(cache, "Sqlym", dummy_create_engine)
    engine = cache.get_database_connection()
    assert isinstance(engine, DummyEngine)
