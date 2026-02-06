"""Cache helpers."""

from __future__ import annotations

from datetime import timedelta

import streamlit as st


@st.cache_data(ttl=timedelta(hours=1))
def load_data(file_path: str):
    import pandas as pd

    return pd.read_csv(file_path)


@st.cache_data(ttl=timedelta(minutes=5))
def fetch_api_data(endpoint: str) -> dict:
    import httpx

    response = httpx.get(endpoint)
    return response.json()


@st.cache_resource
def get_database_connection():
    from sqlalchemy import create_engine

    connection_string = st.secrets["database"]["connection_string"]
    return create_engine(connection_string)
