"""Sidebar components."""

from __future__ import annotations

import streamlit as st


def render_sidebar() -> None:
    st.sidebar.header("メニュー")
    st.sidebar.checkbox("詳細を表示", value=False)
