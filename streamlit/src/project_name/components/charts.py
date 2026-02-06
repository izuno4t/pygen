"""Chart components."""

from __future__ import annotations

from typing import TYPE_CHECKING

import streamlit as st

if TYPE_CHECKING:
    import pandas as pd


def render_metrics_chart(data: "pd.DataFrame") -> None:
    st.line_chart(data, x="date", y="value")


def render_bar_chart(
    data: "pd.DataFrame",
    x: str,
    y: str,
    title: str | None = None,
) -> None:
    if title:
        st.subheader(title)
    st.bar_chart(data, x=x, y=y)
