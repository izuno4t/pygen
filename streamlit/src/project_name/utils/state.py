"""Session state helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, TypeVar

import streamlit as st

T = TypeVar("T")


@dataclass
class AppState:
    user_id: str | None = None
    selected_page: str = "home"
    filters: dict[str, Any] = field(default_factory=dict)
    data_cache: dict[str, Any] = field(default_factory=dict)


def init_session_state() -> None:
    defaults: dict[str, Any] = {
        "initialized": True,
        "user_id": None,
        "selected_filters": {},
        "data_loaded": False,
    }

    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value


def get_state(key: str, default: T | None = None) -> T | None:
    return st.session_state.get(key, default)


def set_state(key: str, value: Any) -> None:
    st.session_state[key] = value


def clear_state(*keys: str) -> None:
    if not keys:
        for key in list(st.session_state.keys()):
            del st.session_state[key]
    else:
        for key in keys:
            if key in st.session_state:
                del st.session_state[key]
