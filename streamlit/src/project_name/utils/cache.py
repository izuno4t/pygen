"""Cache helpers."""

from __future__ import annotations

import pickle
from datetime import timedelta
from pathlib import Path
from typing import TYPE_CHECKING, Any

import httpx
import pandas as pd
import streamlit as st
from sqlym import Sqlym


if TYPE_CHECKING:
    from pandas import DataFrame


@st.cache_data(ttl=timedelta(hours=1))
def load_data(file_path: str) -> DataFrame:
    """CSVファイルを読み込む(1時間キャッシュ)。"""
    return pd.read_csv(file_path)


@st.cache_data(ttl=timedelta(minutes=5))
def fetch_api_data(endpoint: str) -> dict[str, Any]:
    """APIからデータを取得する(5分キャッシュ)。"""
    response = httpx.get(endpoint)
    data: dict[str, Any] = response.json()
    return data


@st.cache_resource
def get_database_connection() -> Any:
    """データベース接続を取得する(アプリ起動中キャッシュ)。"""
    connection_string = st.secrets["database"]["connection_string"]
    return Sqlym(connection_string)


@st.cache_resource
def load_ml_model() -> object:
    """機械学習モデルを読み込む。"""
    model_path = Path("models/model.pkl")
    with model_path.open("rb") as f:
        return pickle.load(f)
