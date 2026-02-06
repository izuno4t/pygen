"""Component tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
import streamlit as st

from project_name.components import charts, forms, sidebar


if TYPE_CHECKING:
    import pytest


def test_render_metrics_chart(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = {}

    def dummy_line_chart(data, x=None, y=None):
        calls["called"] = True

    monkeypatch.setattr(st, "line_chart", dummy_line_chart)

    df = pd.DataFrame({"date": ["2024-01-01"], "value": [1]})
    charts.render_metrics_chart(df)
    assert calls.get("called") is True


def test_render_bar_chart(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = {}

    def dummy_bar_chart(data, x=None, y=None):
        calls["called"] = True

    def dummy_subheader(_title):
        calls["title"] = True

    monkeypatch.setattr(st, "bar_chart", dummy_bar_chart)
    monkeypatch.setattr(st, "subheader", dummy_subheader)

    df = pd.DataFrame({"x": [1], "y": [2]})
    charts.render_bar_chart(df, x="x", y="y", title="t")
    assert calls.get("called") is True
    assert calls.get("title") is True


def test_render_forms_sidebar(monkeypatch: pytest.MonkeyPatch) -> None:
    class DummyForm:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def text_input(self, *_args, **_kwargs):
            return ""

        def text_area(self, *_args, **_kwargs):
            return ""

        def form_submit_button(self, *_args, **_kwargs):
            return False

    monkeypatch.setattr(st, "form", lambda _name: DummyForm())
    monkeypatch.setattr(st, "success", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(st, "sidebar", st)
    monkeypatch.setattr(st, "header", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(st, "checkbox", lambda *_args, **_kwargs: None)

    forms.render_contact_form()
    sidebar.render_sidebar()
