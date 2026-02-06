# Python Webアプリケーション ボイラープレート仕様書

## Streamlit編

**作成日**: 2025年1月  
**対象**: Python 3.11+ / Streamlit 1.30+  
**前提**: 「汎用プロジェクトスタイル編」の内容を継承

---

## 1. 概要

### 1.1 本仕様書の目的

汎用プロジェクトスタイルを基盤として、Streamlit固有の設定・構成・ベストプラクティスを定義する。

### 1.2 Streamlitの特徴

| 特徴 | 説明 |
|------|------|
| スクリプト実行モデル | ユーザー操作のたびにスクリプト全体が再実行される |
| セッション状態 | `st.session_state` で再実行間のデータを保持 |
| マルチページ対応 | `st.navigation` / `st.Page` または `pages/` ディレクトリ |
| 設定ファイル | `.streamlit/config.toml` と `secrets.toml` |

---

## 2. ディレクトリ構造

### 2.1 推奨構造（マルチページアプリ）

```
project-name/
├── .devcontainer/                 # Dev Container設定（オプション）
│   └── devcontainer.json
├── .streamlit/                    # Streamlit設定
│   ├── config.toml                # アプリ設定
│   └── secrets.toml.example       # シークレットのテンプレート（実体はgitignore）
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── app.py                 # エントリポイント（streamlit run）
│       ├── pages/                 # ページモジュール
│       │   ├── __init__.py
│       │   ├── home.py
│       │   ├── dashboard.py
│       │   └── settings.py
│       ├── components/            # 再利用可能なUIコンポーネント
│       │   ├── __init__.py
│       │   ├── sidebar.py
│       │   ├── charts.py
│       │   └── forms.py
│       ├── services/              # ビジネスロジック・外部API連携
│       │   ├── __init__.py
│       │   ├── data_service.py
│       │   └── api_client.py
│       ├── models/                # データモデル（Pydantic等）
│       │   ├── __init__.py
│       │   └── schemas.py
│       ├── utils/                 # ユーティリティ
│       │   ├── __init__.py
│       │   ├── state.py           # セッション状態ヘルパー
│       │   └── cache.py           # キャッシュユーティリティ
│       └── config.py              # アプリ設定読み込み
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/                      # ユニットテスト
│   │   └── test_services.py
│   └── integration/
│       └── test_services.py
├── data/                          # ローカルデータ（オプション）
│   └── .gitkeep
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── Makefile
├── pyproject.toml
├── uv.lock
├── README.md
└── LICENSE
```

### 2.2 シンプル構造（単一ページ / 小規模アプリ）

```
project-name/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── app.py                 # メインアプリ
│       ├── components.py          # UIコンポーネント
│       └── utils.py               # ユーティリティ
├── tests/
├── .gitignore
├── Makefile
├── pyproject.toml
└── README.md
```

---

## 3. Streamlit設定ファイル

### 3.1 `.streamlit/config.toml`

```toml
[global]
developmentMode = false

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[client]
showErrorDetails = true
toolbarMode = "auto"
```

### 3.2 `.streamlit/secrets.toml.example`

```toml
# このファイルをコピーして secrets.toml を作成
# secrets.toml は .gitignore に含めること

[database]
host = "localhost"
port = 5432
user = "your_username"
password = "your_password"
database = "your_database"

[api]
openai_key = "sk-..."
anthropic_key = "sk-ant-..."

[auth]
admin_password = "change_me"
```

### 3.3 シークレット管理のルール

| ファイル | Git管理 | 用途 |
|---------|--------|------|
| `secrets.toml.example` | ✅ 含める | テンプレート |
| `secrets.toml` | ❌ 除外 | 実際のシークレット |
| `.env` | ❌ 除外 | 環境変数（代替手段） |

---

## 4. pyproject.toml への追加設定

汎用仕様書の設定に以下を追加：

```toml
[project]
name = "project-name"
version = "0.1.0"
# ... 汎用設定 ...

dependencies = [
    "streamlit>=1.30",
    "pydantic>=2.0",
    "pandas>=2.0",
    # 必要に応じて追加
    # "plotly>=5.0",
    # "altair>=5.0",
    # "sqlalchemy>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=4.0",
    "mypy>=1.8",
    "ruff>=0.4",
    "pre-commit>=3.6",
    "pandas-stubs",  # pandasの型スタブ
]

[project.scripts]
# Streamlitアプリの起動スクリプト
app = "project_name.app:main"
```

### 4.1 Ruff追加設定

```toml
[tool.ruff.lint]
# 汎用設定に追加
extend-ignore = [
    "B008",   # function call in default argument (Streamlit Depends対応)
]

[tool.ruff.lint.per-file-ignores]
"src/**/pages/*.py" = [
    "E402",   # module level import not at top of file (Streamlitのページ構造対応)
]
```

### 4.2 mypy追加設定

```toml
[[tool.mypy.overrides]]
module = "streamlit.*"
ignore_missing_imports = true
```

---

## 5. Makefile（Streamlit版）

```makefile
.PHONY: help install dev test lint format typecheck check clean run

# デフォルトターゲット
help:
	@echo "Available commands:"
	@echo "  make install    - Install production dependencies"
	@echo "  make dev        - Install all dependencies (including dev)"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linter"
	@echo "  make format     - Format code"
	@echo "  make typecheck  - Run type checker"
	@echo "  make check      - Run all checks (lint, typecheck, test)"
	@echo "  make run        - Run Streamlit app"
	@echo "  make clean      - Remove build artifacts"

# 依存関係
install:
	uv sync

dev:
	uv sync --dev
	uv run pre-commit install
	@echo "Don't forget to copy .streamlit/secrets.toml.example to .streamlit/secrets.toml"

# テスト
test:
	uv run pytest

# コード品質
lint:
	uv run ruff check .

format:
	uv run ruff format .
	uv run ruff check --fix .

typecheck:
	uv run mypy .

check: lint typecheck test

# Streamlitアプリ実行
run:
	uv run streamlit run src/project_name/app.py

run-dev:
	uv run streamlit run src/project_name/app.py --server.runOnSave=true

# クリーンアップ
clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
```

---

## 6. アプリ実装パターン

### 6.1 エントリポイント (`app.py`)

#### パターン1: st.navigation（推奨）

```python
"""Streamlitアプリケーションのエントリポイント。"""

from __future__ import annotations

import streamlit as st

from project_name.pages import dashboard, home, settings
from project_name.utils.state import init_session_state


def main() -> None:
    """アプリケーションのメイン関数。"""
    # ページ設定（最初に呼び出す必要あり）
    st.set_page_config(
        page_title="My App",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # セッション状態の初期化
    init_session_state()

    # ページ定義
    pages = [
        st.Page(home.render, title="ホーム", icon="🏠", default=True),
        st.Page(dashboard.render, title="ダッシュボード", icon="📊"),
        st.Page(settings.render, title="設定", icon="⚙️"),
    ]

    # ナビゲーション
    pg = st.navigation(pages)
    pg.run()


if __name__ == "__main__":
    main()
```

#### パターン2: pages/ ディレクトリ（シンプル）

```python
"""Streamlitアプリケーションのエントリポイント（pages/ディレクトリ使用）。"""

from __future__ import annotations

import streamlit as st

from project_name.utils.state import init_session_state


def main() -> None:
    """アプリケーションのメイン関数。"""
    st.set_page_config(
        page_title="My App",
        page_icon="🚀",
        layout="wide",
    )

    init_session_state()

    st.title("🏠 ホーム")
    st.write("Welcome to My App!")


if __name__ == "__main__":
    main()
```

この場合、`src/project_name/pages/` 内のファイルが自動的にページとして認識される。

### 6.2 ページモジュール (`pages/dashboard.py`)

```python
"""ダッシュボードページ。"""

from __future__ import annotations

import streamlit as st

from project_name.components.charts import render_metrics_chart
from project_name.services.data_service import get_dashboard_data


def render() -> None:
    """ダッシュボードページをレンダリングする。"""
    st.title("📊 ダッシュボード")

    # データ取得（キャッシュ付き）
    data = get_dashboard_data()

    # メトリクス表示
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("総ユーザー数", data.total_users, delta=data.user_delta)
    with col2:
        st.metric("アクティブ数", data.active_users)
    with col3:
        st.metric("コンバージョン率", f"{data.conversion_rate:.1%}")

    # チャート表示
    st.subheader("トレンド")
    render_metrics_chart(data.trend_data)
```

### 6.3 再利用可能コンポーネント (`components/charts.py`)

```python
"""チャートコンポーネント。"""

from __future__ import annotations

from typing import TYPE_CHECKING

import streamlit as st

if TYPE_CHECKING:
    import pandas as pd


def render_metrics_chart(data: pd.DataFrame) -> None:
    """メトリクスチャートを描画する。

    Args:
        data: チャート用データフレーム（columns: date, value）
    """
    st.line_chart(data, x="date", y="value")


def render_bar_chart(
    data: pd.DataFrame,
    x: str,
    y: str,
    title: str | None = None,
) -> None:
    """バーチャートを描画する。

    Args:
        data: チャート用データフレーム
        x: X軸のカラム名
        y: Y軸のカラム名
        title: チャートタイトル
    """
    if title:
        st.subheader(title)
    st.bar_chart(data, x=x, y=y)
```

---

## 7. セッション状態管理

### 7.1 状態管理ヘルパー (`utils/state.py`)

```python
"""セッション状態管理ユーティリティ。"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, TypeVar

import streamlit as st

T = TypeVar("T")


@dataclass
class AppState:
    """アプリケーションの状態を定義するデータクラス。"""

    user_id: str | None = None
    selected_page: str = "home"
    filters: dict[str, Any] = field(default_factory=dict)
    data_cache: dict[str, Any] = field(default_factory=dict)


def init_session_state() -> None:
    """セッション状態を初期化する。"""
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
    """セッション状態から値を取得する。

    Args:
        key: 状態のキー
        default: デフォルト値

    Returns:
        状態の値、存在しない場合はデフォルト値
    """
    return st.session_state.get(key, default)


def set_state(key: str, value: Any) -> None:
    """セッション状態に値を設定する。

    Args:
        key: 状態のキー
        value: 設定する値
    """
    st.session_state[key] = value


def clear_state(*keys: str) -> None:
    """指定したキーの状態をクリアする。

    Args:
        keys: クリアするキー（指定なしで全クリア）
    """
    if not keys:
        for key in list(st.session_state.keys()):
            del st.session_state[key]
    else:
        for key in keys:
            if key in st.session_state:
                del st.session_state[key]
```

### 7.2 状態管理のベストプラクティス

```python
"""セッション状態の使用例。"""

import streamlit as st


# ✅ 良い例: 初期化チェックを行う
def good_example() -> None:
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    if st.button("カウントアップ"):
        st.session_state.counter += 1

    st.write(f"カウント: {st.session_state.counter}")


# ❌ 悪い例: 初期化チェックなし（毎回リセットされる）
def bad_example() -> None:
    counter = 0  # 再実行のたびに0にリセット

    if st.button("カウントアップ"):
        counter += 1  # 意味がない

    st.write(f"カウント: {counter}")


# ✅ コールバックを使った状態更新
def callback_example() -> None:
    def on_change() -> None:
        st.session_state.processed = True

    st.text_input(
        "入力",
        key="user_input",
        on_change=on_change,
    )

    if st.session_state.get("processed"):
        st.success("入力が処理されました")
```

---

## 8. キャッシュ戦略

### 8.1 データキャッシュ (`@st.cache_data`)

```python
"""データキャッシュの使用例。"""

from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

import streamlit as st

if TYPE_CHECKING:
    import pandas as pd


@st.cache_data(ttl=timedelta(hours=1))
def load_data(file_path: str) -> pd.DataFrame:
    """CSVファイルを読み込む（1時間キャッシュ）。

    Args:
        file_path: ファイルパス

    Returns:
        読み込んだデータフレーム
    """
    import pandas as pd

    return pd.read_csv(file_path)


@st.cache_data(ttl=timedelta(minutes=5))
def fetch_api_data(endpoint: str) -> dict:
    """APIからデータを取得する（5分キャッシュ）。

    Args:
        endpoint: APIエンドポイント

    Returns:
        APIレスポンス
    """
    import httpx

    response = httpx.get(endpoint)
    return response.json()
```

### 8.2 リソースキャッシュ (`@st.cache_resource`)

```python
"""リソースキャッシュの使用例。"""

from __future__ import annotations

import streamlit as st


@st.cache_resource
def get_database_connection():
    """データベース接続を取得する（アプリ起動中キャッシュ）。

    Returns:
        データベース接続オブジェクト
    """
    from sqlalchemy import create_engine

    connection_string = st.secrets["database"]["connection_string"]
    return create_engine(connection_string)


@st.cache_resource
def load_ml_model():
    """機械学習モデルを読み込む。

    Returns:
        読み込んだモデル
    """
    import pickle
    from pathlib import Path

    model_path = Path("models/model.pkl")
    with model_path.open("rb") as f:
        return pickle.load(f)
```

### 8.3 キャッシュ使い分け

| デコレータ | 用途 | キャッシュ範囲 |
|-----------|------|--------------|
| `@st.cache_data` | データ（DataFrame、dict等） | 全ユーザー共有 |
| `@st.cache_resource` | リソース（DB接続、MLモデル等） | 全ユーザー共有 |
| `st.session_state` | ユーザー固有の状態 | セッション単位 |

---

## 9. 設定管理 (`config.py`)

```python
"""アプリケーション設定。"""

from __future__ import annotations

from functools import lru_cache
from typing import Any

import streamlit as st
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """アプリケーション設定。"""

    # アプリ設定
    app_name: str = "My Streamlit App"
    debug: bool = False

    # API設定
    api_base_url: str = "https://api.example.com"
    api_timeout: int = 30

    # データベース設定（secrets.tomlから読み込む場合は別途処理）
    database_url: str | None = None

    class Config:
        env_prefix = "APP_"
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    """設定を取得する（シングルトン）。

    Returns:
        アプリケーション設定
    """
    return Settings()


def get_secret(key: str, default: Any = None) -> Any:
    """Streamlitシークレットから値を取得する。

    Args:
        key: シークレットのキー（ドット区切りで階層指定可能）
        default: デフォルト値

    Returns:
        シークレットの値
    """
    try:
        keys = key.split(".")
        value = st.secrets
        for k in keys:
            value = value[k]
        return value
    except (KeyError, FileNotFoundError):
        return default
```

---

## 10. テスト

### 10.1 Streamlitアプリのテスト戦略

| レイヤー | テスト方法 | ツール |
|---------|----------|--------|
| ビジネスロジック | ユニットテスト | pytest |
| データ処理 | ユニットテスト | pytest + pandas |
| UIコンポーネント | 限定的（ロジック分離推奨） | - |
| E2E | 必要に応じて | Playwright |

### 10.2 テスト例

```python
"""サービス層のテスト例。"""

from __future__ import annotations

import pytest

from project_name.services.data_service import calculate_metrics, validate_input


class TestDataService:
    """DataServiceのテスト。"""

    def test_calculate_metrics_normal(self) -> None:
        """正常なメトリクス計算をテストする。"""
        data = [10, 20, 30, 40, 50]
        result = calculate_metrics(data)

        assert result.mean == 30
        assert result.total == 150

    def test_calculate_metrics_empty(self) -> None:
        """空データでのメトリクス計算をテストする。"""
        with pytest.raises(ValueError, match="データが空です"):
            calculate_metrics([])

    @pytest.mark.parametrize(
        ("input_value", "expected"),
        [
            ("valid@example.com", True),
            ("invalid-email", False),
            ("", False),
        ],
    )
    def test_validate_input(self, input_value: str, expected: bool) -> None:
        """入力バリデーションをテストする。"""
        assert validate_input(input_value) == expected
```

### 10.3 conftest.py

```python
"""pytest設定。"""

from __future__ import annotations

from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def mock_streamlit() -> Generator[MagicMock, None, None]:
    """Streamlitをモックする。"""
    with patch("streamlit.session_state", {}) as mock:
        yield mock


@pytest.fixture
def sample_dataframe():
    """テスト用DataFrameを提供する。"""
    import pandas as pd

    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=10),
        "value": range(10),
    })
```

---

## 11. デプロイ

### 11.1 Streamlit Community Cloud

1. GitHubリポジトリをStreamlit Community Cloudに接続
2. メインファイルパスを指定: `src/project_name/app.py`
3. シークレットを設定画面で入力（`secrets.toml`の内容）

### 11.2 Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# uv インストール
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# 依存関係インストール
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# アプリケーションコピー
COPY src/ ./src/
COPY .streamlit/ ./.streamlit/

# ポート公開
EXPOSE 8501

# ヘルスチェック
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# 実行
ENTRYPOINT ["uv", "run", "streamlit", "run", "src/project_name/app.py", \
    "--server.port=8501", "--server.address=0.0.0.0"]
```

### 11.3 docker-compose.yml

```yaml
version: "3.8"

services:
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
    volumes:
      - ./.streamlit/secrets.toml:/app/.streamlit/secrets.toml:ro
    restart: unless-stopped
```

---

## 12. .gitignore への追加

汎用仕様書の`.gitignore`に以下を追加：

```gitignore
# Streamlit
.streamlit/secrets.toml

# Data
data/*.csv
data/*.xlsx
data/*.json
!data/.gitkeep
```

---

## 13. セットアップ手順

```bash
# 1. 汎用仕様書のセットアップを実行後...

# 2. Streamlit固有の設定
mkdir -p .streamlit
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# secrets.toml を編集

# 3. 開発サーバー起動
make run

# または
uv run streamlit run src/project_name/app.py
```

---

## 付録A: チェックリスト

### 新規プロジェクト作成時

- [ ] 汎用プロジェクト構造を作成
- [ ] `.streamlit/config.toml` を設定
- [ ] `.streamlit/secrets.toml.example` を作成
- [ ] `secrets.toml` を `.gitignore` に追加
- [ ] `app.py` エントリポイントを作成
- [ ] セッション状態の初期化処理を実装
- [ ] Makefileに `run` ターゲットを追加

### デプロイ前

- [ ] シークレットが正しく設定されているか確認
- [ ] `config.toml` の本番設定を確認
- [ ] 不要なデバッグコードを削除
- [ ] `st.set_page_config()` が最初に呼ばれているか確認

---

## 付録B: よく使うStreamlit API

| API | 用途 |
|-----|------|
| `st.set_page_config()` | ページ設定（タイトル、アイコン、レイアウト） |
| `st.navigation()` / `st.Page()` | マルチページナビゲーション |
| `st.session_state` | セッション状態管理 |
| `st.cache_data` | データキャッシュ |
| `st.cache_resource` | リソースキャッシュ |
| `st.secrets` | シークレット読み込み |
| `st.columns()` | カラムレイアウト |
| `st.tabs()` | タブUI |
| `st.expander()` | 折りたたみUI |
| `st.form()` | フォーム（まとめて送信） |
| `st.rerun()` | 強制再実行 |

---

**改訂履歴**

| バージョン | 日付 | 内容 |
|-----------|------|------|
| 1.0 | 2025-01 | 初版作成 |
