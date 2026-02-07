"""Page and app tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

import streamlit as st

from project_name import app
from project_name.pages import dashboard, home, settings


if TYPE_CHECKING:
    import pytest


def test_page_renderers(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: dict[str, list[str]] = {"title": []}

    def dummy_title(value):
        calls["title"].append(value)

    monkeypatch.setattr(st, "title", dummy_title)

    home.render()
    dashboard.render()
    settings.render()

    assert "ホーム" in calls["title"]
    assert "ダッシュボード" in calls["title"]
    assert "設定" in calls["title"]


def test_app_main(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: dict[str, bool] = {"set": False, "run": False}

    monkeypatch.setattr(
        st,
        "set_page_config",
        lambda **_kwargs: calls.__setitem__("set", True),
    )
    monkeypatch.setattr(st, "session_state", {})

    class DummyPage:
        def __init__(self, _fn, title=None, icon=None, default=False):
            self.title = title

    class DummyNav:
        def run(self):
            calls["run"] = True

    def dummy_navigation(_pages):
        return DummyNav()

    monkeypatch.setattr(st, "Page", DummyPage)
    monkeypatch.setattr(st, "navigation", dummy_navigation)

    app.main()

    assert calls["set"] is True
    assert calls["run"] is True
