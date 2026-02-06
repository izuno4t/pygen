"""Chart components."""

from __future__ import annotations

from typing import TYPE_CHECKING

import streamlit as st


if TYPE_CHECKING:
    from pandas import DataFrame


def render_metrics_chart(data: DataFrame) -> None:
    st.line_chart(data, x="date", y="value")


def render_bar_chart(
    data: DataFrame,
    x: str,
    y: str,
    title: str | None = None,
) -> None:
    if title:
        st.subheader(title)
    st.bar_chart(data, x=x, y=y)
