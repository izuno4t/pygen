"""Session state tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

import streamlit as st

from project_name.utils import state


if TYPE_CHECKING:
    import pytest


def test_state_helpers(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(st, "session_state", {})

    state.init_session_state()
    assert st.session_state["initialized"] is True

    state.set_state("foo", "bar")
    assert state.get_state("foo") == "bar"

    state.clear_state("foo")
    assert state.get_state("foo") is None
