"""Service tests."""

from __future__ import annotations

import httpx
import pytest

from project_name.services import api_client, data_service


def test_calculate_metrics_normal() -> None:
    result = data_service.calculate_metrics([10, 20, 30])
    assert result.total == 60
    assert result.mean == 20


def test_calculate_metrics_empty() -> None:
    with pytest.raises(ValueError, match="データが空です"):
        data_service.calculate_metrics([])


def test_fetch_status(monkeypatch: pytest.MonkeyPatch) -> None:
    class DummyResponse:
        def json(self):
            return {"ok": True}

        def raise_for_status(self):
            return None

    def dummy_get(_endpoint, timeout=10):
        return DummyResponse()

    monkeypatch.setattr(httpx, "get", dummy_get)
    result = api_client.fetch_status("https://example.com")
    assert result["ok"] is True
