# Python Webアプリケーション ボイラープレート仕様書

## FastAPI編

**作成日**: 2025年1月  
**対象**: Python 3.11+ / FastAPI 0.110+  
**前提**: 「汎用プロジェクトスタイル編」の内容を継承

---

## 1. 概要

### 1.1 本仕様書の目的

汎用プロジェクトスタイルを基盤として、FastAPI固有の設定・構成・ベストプラクティスを定義する。

### 1.2 FastAPIの特徴

| 特徴 | 説明 |
|------|------|
| 非同期ファースト | ASGI対応、async/await による高性能 |
| 型ヒント活用 | Pydanticによる自動バリデーション |
| 依存性注入 | `Depends()` による柔軟なDIシステム |
| 自動ドキュメント | OpenAPI (Swagger UI / ReDoc) 自動生成 |

### 1.3 プロジェクト構造の選択

| 構造 | 用途 | 推奨 |
|------|------|------|
| ファイルタイプ別 | マイクロサービス、小規模 | 小〜中規模 |
| ドメイン別 | モノリス、大規模 | 中〜大規模 |

本仕様書では両方のパターンを提示する。

---

## 2. ディレクトリ構造

### 2.1 ファイルタイプ別構造（小〜中規模）

```
project-name/
├── .devcontainer/                 # Dev Container設定（オプション）
│   └── devcontainer.json
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── main.py                # エントリポイント
│       ├── dependencies.py        # 共通依存性
│       ├── routers/               # APIルーター
│       │   ├── __init__.py
│       │   ├── users.py
│       │   ├── items.py
│       │   └── health.py
│       ├── schemas/               # Pydanticスキーマ（リクエスト/レスポンス）
│       │   ├── __init__.py
│       │   ├── user.py
│       │   └── item.py
│       ├── models/                # DBモデル（SQLAlchemy等）
│       │   ├── __init__.py
│       │   ├── user.py
│       │   └── item.py
│       ├── services/              # ビジネスロジック
│       │   ├── __init__.py
│       │   ├── user_service.py
│       │   └── item_service.py
│       ├── repositories/          # データアクセス層
│       │   ├── __init__.py
│       │   └── base.py
│       ├── core/                  # アプリケーション設定
│       │   ├── __init__.py
│       │   ├── config.py          # Pydantic Settings
│       │   ├── security.py        # 認証・認可
│       │   └── database.py        # DB接続
│       └── utils/                 # ユーティリティ
│           ├── __init__.py
│           └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   └── test_services.py
│   └── integration/
│       └── test_api.py
├── alembic/                       # DBマイグレーション（オプション）
│   ├── versions/
│   └── env.py
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── alembic.ini                    # Alembic設定（オプション）
├── Makefile
├── pyproject.toml
├── uv.lock
├── README.md
└── LICENSE
```

### 2.2 ドメイン別構造（中〜大規模）

Netflix Dispatch インスパイアの構造。各ドメインが独立したモジュールとして機能。

```
project-name/
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── main.py                # エントリポイント
│       ├── core/                  # グローバル設定
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── database.py
│       │   ├── security.py
│       │   └── exceptions.py      # グローバル例外
│       ├── auth/                  # 認証ドメイン
│       │   ├── __init__.py
│       │   ├── router.py
│       │   ├── schemas.py
│       │   ├── models.py
│       │   ├── service.py
│       │   ├── dependencies.py
│       │   ├── constants.py
│       │   └── exceptions.py
│       ├── users/                 # ユーザードメイン
│       │   ├── __init__.py
│       │   ├── router.py
│       │   ├── schemas.py
│       │   ├── models.py
│       │   ├── service.py
│       │   ├── dependencies.py
│       │   └── exceptions.py
│       └── items/                 # アイテムドメイン
│           ├── __init__.py
│           ├── router.py
│           ├── schemas.py
│           ├── models.py
│           ├── service.py
│           └── dependencies.py
├── tests/
├── alembic/
└── ...
```

### 2.3 ドメイン別構造の各ファイル役割

| ファイル | 役割 |
|---------|------|
| `router.py` | APIエンドポイント定義 |
| `schemas.py` | リクエスト/レスポンスのPydanticモデル |
| `models.py` | DBモデル（SQLAlchemy等） |
| `service.py` | ビジネスロジック |
| `dependencies.py` | ドメイン固有の依存性 |
| `constants.py` | 定数定義 |
| `exceptions.py` | ドメイン固有の例外 |

---

## 3. pyproject.toml への追加設定

汎用仕様書の設定に以下を追加：

```toml
[project]
name = "project-name"
version = "0.1.0"
# ... 汎用設定 ...

dependencies = [
    "fastapi>=0.110",
    "uvicorn[standard]>=0.27",
    "pydantic>=2.0",
    "pydantic-settings>=2.0",
    # DB関連（必要に応じて）
    # "sqlalchemy>=2.0",
    # "asyncpg>=0.29",          # PostgreSQL async
    # "alembic>=1.13",          # マイグレーション
    # 認証関連（必要に応じて）
    # "python-jose[cryptography]>=3.3",
    # "passlib[bcrypt]>=1.7",
    # HTTP クライアント（必要に応じて）
    # "httpx>=0.27",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=4.0",
    "pytest-asyncio>=0.23",
    "httpx>=0.27",             # TestClient用
    "mypy>=1.8",
    "ruff>=0.4",
    "pre-commit>=3.6",
]

[project.scripts]
# 開発サーバー起動
dev = "uvicorn project_name.main:app --reload"
```

### 3.1 pytest追加設定

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
```

### 3.2 Ruff追加設定

```toml
[tool.ruff.lint]
extend-ignore = [
    "B008",   # function call in default argument (FastAPI Depends対応)
]
```

---

## 4. Makefile（FastAPI版）

```makefile
.PHONY: help install dev test lint format typecheck check clean run migrate

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
	@echo "  make run        - Run development server"
	@echo "  make run-prod   - Run production server"
	@echo "  make migrate    - Run database migrations"
	@echo "  make clean      - Remove build artifacts"

# 依存関係
install:
	uv sync

dev:
	uv sync --dev
	uv run pre-commit install

# テスト
test:
	uv run pytest

test-cov:
	uv run pytest --cov --cov-report=html --cov-report=term-missing

# コード品質
lint:
	uv run ruff check .

format:
	uv run ruff format .
	uv run ruff check --fix .

typecheck:
	uv run mypy .

check: lint typecheck test

# サーバー実行
run:
	uv run uvicorn src.project_name.main:app --reload --host 0.0.0.0 --port 8000

run-prod:
	uv run uvicorn src.project_name.main:app --host 0.0.0.0 --port 8000 --workers 4

# DBマイグレーション（Alembic使用時）
migrate:
	uv run alembic upgrade head

migrate-new:
	@read -p "Migration message: " msg; \
	uv run alembic revision --autogenerate -m "$$msg"

# クリーンアップ
clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
```

---

## 5. 設定管理 (`core/config.py`)

### 5.1 Pydantic Settings

```python
"""アプリケーション設定。"""

from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import Field, PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """アプリケーション設定。

    環境変数または .env ファイルから読み込む。
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # アプリケーション設定
    app_name: str = "FastAPI App"
    app_version: str = "0.1.0"
    debug: bool = False
    environment: Literal["development", "staging", "production"] = "development"

    # API設定
    api_v1_prefix: str = "/api/v1"
    allowed_hosts: list[str] = Field(default_factory=lambda: ["*"])

    # セキュリティ設定
    secret_key: str = Field(..., min_length=32)
    access_token_expire_minutes: int = 30
    algorithm: str = "HS256"

    # データベース設定
    database_url: PostgresDsn | None = None

    # CORS設定
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    @computed_field
    @property
    def is_development(self) -> bool:
        """開発環境かどうかを判定する。"""
        return self.environment == "development"


@lru_cache
def get_settings() -> Settings:
    """設定を取得する（シングルトン）。

    Returns:
        アプリケーション設定
    """
    return Settings()
```

### 5.2 .env.example

```bash
# Application
APP_NAME="My FastAPI App"
APP_VERSION="0.1.0"
DEBUG=true
ENVIRONMENT=development

# Security
SECRET_KEY=your-super-secret-key-at-least-32-characters

# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname

# CORS
CORS_ORIGINS=["http://localhost:3000","http://localhost:8080"]
```

---

## 6. アプリ実装パターン

### 6.1 エントリポイント (`main.py`)

```python
"""FastAPIアプリケーションのエントリポイント。"""

from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from project_name.core.config import get_settings
from project_name.routers import health, items, users

if TYPE_CHECKING:
    from project_name.core.config import Settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """アプリケーションのライフサイクル管理。

    起動時・終了時の処理をここに記述する。
    """
    # 起動時の処理
    settings = get_settings()
    print(f"Starting {settings.app_name} ({settings.environment})")
    # DB接続プール作成など

    yield

    # 終了時の処理
    print("Shutting down...")
    # DB接続クローズなど


def create_app(settings: Settings | None = None) -> FastAPI:
    """FastAPIアプリケーションを作成する。

    Args:
        settings: アプリケーション設定（テスト時のオーバーライド用）

    Returns:
        FastAPIアプリケーションインスタンス
    """
    if settings is None:
        settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        openapi_url=f"{settings.api_v1_prefix}/openapi.json",
        docs_url=f"{settings.api_v1_prefix}/docs",
        redoc_url=f"{settings.api_v1_prefix}/redoc",
        lifespan=lifespan,
    )

    # ミドルウェア設定
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ルーター登録
    app.include_router(health.router, tags=["health"])
    app.include_router(
        users.router,
        prefix=f"{settings.api_v1_prefix}/users",
        tags=["users"],
    )
    app.include_router(
        items.router,
        prefix=f"{settings.api_v1_prefix}/items",
        tags=["items"],
    )

    return app


# アプリケーションインスタンス
app = create_app()
```

### 6.2 ルーター (`routers/users.py`)

```python
"""ユーザー関連のAPIエンドポイント。"""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from project_name.schemas.user import UserCreate, UserRead, UserUpdate
from project_name.services.user_service import UserService

router = APIRouter()


def get_user_service() -> UserService:
    """UserServiceの依存性を提供する。"""
    return UserService()


UserServiceDep = Annotated[UserService, Depends(get_user_service)]


@router.get("/", response_model=list[UserRead])
async def list_users(
    service: UserServiceDep,
    skip: int = 0,
    limit: int = 100,
) -> list[UserRead]:
    """ユーザー一覧を取得する。"""
    return await service.get_users(skip=skip, limit=limit)


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    service: UserServiceDep,
) -> UserRead:
    """新規ユーザーを作成する。"""
    return await service.create_user(user_in)


@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: int,
    service: UserServiceDep,
) -> UserRead:
    """指定したIDのユーザーを取得する。"""
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.patch("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: int,
    user_in: UserUpdate,
    service: UserServiceDep,
) -> UserRead:
    """ユーザー情報を更新する。"""
    user = await service.update_user(user_id, user_in)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    service: UserServiceDep,
) -> None:
    """ユーザーを削除する。"""
    deleted = await service.delete_user(user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
```

### 6.3 ヘルスチェック (`routers/health.py`)

```python
"""ヘルスチェックエンドポイント。"""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    """ヘルスチェックレスポンス。"""

    status: str
    version: str


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """アプリケーションのヘルスステータスを返す。"""
    from project_name.core.config import get_settings

    settings = get_settings()
    return HealthResponse(status="healthy", version=settings.app_version)


@router.get("/ready")
async def readiness_check() -> dict[str, str]:
    """Kubernetes Readiness Probe用エンドポイント。"""
    # DB接続チェックなどを追加
    return {"status": "ready"}
```

---

## 7. Pydanticスキーマ (`schemas/user.py`)

```python
"""ユーザー関連のPydanticスキーマ。"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """ユーザーの基本スキーマ。"""

    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)
    is_active: bool = True


class UserCreate(UserBase):
    """ユーザー作成スキーマ。"""

    password: str = Field(..., min_length=8, max_length=100)


class UserUpdate(BaseModel):
    """ユーザー更新スキーマ（部分更新対応）。"""

    email: EmailStr | None = None
    name: str | None = Field(None, min_length=1, max_length=100)
    is_active: bool | None = None
    password: str | None = Field(None, min_length=8, max_length=100)


class UserRead(UserBase):
    """ユーザー読み取りスキーマ（レスポンス用）。"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
```

---

## 8. 依存性注入パターン

### 8.1 共通依存性 (`dependencies.py`)

```python
"""共通の依存性定義。"""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import Depends, Header, HTTPException, status

from project_name.core.config import Settings, get_settings


# 設定の依存性
SettingsDep = Annotated[Settings, Depends(get_settings)]


# ページネーションパラメータ
class PaginationParams:
    """ページネーションパラメータ。"""

    def __init__(
        self,
        skip: int = 0,
        limit: int = 100,
    ) -> None:
        if limit > 1000:
            limit = 1000
        self.skip = skip
        self.limit = limit


PaginationDep = Annotated[PaginationParams, Depends()]


# 認証依存性（例）
async def get_current_user(
    authorization: Annotated[str | None, Header()] = None,
    settings: SettingsDep = None,
) -> dict[str, Any]:
    """現在のユーザーを取得する。

    Args:
        authorization: Authorizationヘッダー
        settings: アプリケーション設定

    Returns:
        ユーザー情報

    Raises:
        HTTPException: 認証エラー時
    """
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header required",
        )

    # トークン検証ロジック
    # ...

    return {"user_id": 1, "email": "user@example.com"}


CurrentUserDep = Annotated[dict[str, Any], Depends(get_current_user)]
```

### 8.2 依存性のベストプラクティス

```python
"""依存性の使用例とベストプラクティス。"""

from typing import Annotated
from fastapi import Depends


# ✅ 良い例: Annotatedを使用した型エイリアス
UserServiceDep = Annotated[UserService, Depends(get_user_service)]


@router.get("/users")
async def list_users(service: UserServiceDep) -> list[User]:
    return await service.get_all()


# ✅ 良い例: 依存性のキャッシュを活用
# FastAPIは同一リクエスト内で依存性をキャッシュする
@router.get("/profile")
async def get_profile(
    user: CurrentUserDep,
    service: UserServiceDep,  # get_user_serviceは1回だけ呼ばれる
) -> UserProfile:
    return await service.get_profile(user["user_id"])


# ❌ 悪い例: デフォルト引数に関数呼び出し（B008警告）
# ただしFastAPIのDepends()は例外として許可
@router.get("/bad")
def bad_example(service=get_user_service()):  # これはNG
    pass
```

---

## 9. 非同期/同期の使い分け

### 9.1 基本ルール

| 状況 | 推奨 | 理由 |
|------|------|------|
| I/Oバウンド（DB、外部API） | `async def` | イベントループをブロックしない |
| CPUバウンド | `def`（同期） | スレッドプールで実行される |
| ブロッキングSDK使用 | `def` + `run_in_executor` | イベントループをブロックしない |

### 9.2 実装例

```python
"""非同期/同期の実装例。"""

from __future__ import annotations

import asyncio
from concurrent.futures import ThreadPoolExecutor

from fastapi import APIRouter

router = APIRouter()


# ✅ 非同期I/O（推奨）
@router.get("/async-io")
async def async_io_operation() -> dict:
    """非同期I/O操作の例。"""
    # 非同期DBクエリ
    result = await async_db_query()
    return {"result": result}


# ✅ 同期関数（CPUバウンド or ブロッキングSDK）
@router.get("/sync-operation")
def sync_operation() -> dict:
    """同期操作の例。FastAPIがスレッドプールで実行する。"""
    # ブロッキング操作
    result = blocking_sdk_call()
    return {"result": result}


# ✅ 非同期ルートでブロッキング処理を実行
@router.get("/mixed")
async def mixed_operation() -> dict:
    """非同期ルートでブロッキング処理を実行する例。"""
    loop = asyncio.get_event_loop()

    # スレッドプールでブロッキング処理を実行
    with ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(
            executor,
            blocking_sdk_call,
        )

    return {"result": result}


# ❌ 悪い例: 非同期ルートでブロッキング
@router.get("/bad")
async def bad_async() -> dict:
    """これはイベントループをブロックする！"""
    result = blocking_sdk_call()  # NG: イベントループがブロックされる
    return {"result": result}
```

---

## 10. テスト

### 10.1 conftest.py

```python
"""pytest設定とフィクスチャ。"""

from __future__ import annotations

from collections.abc import AsyncGenerator, Generator
from typing import Any

import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from project_name.core.config import Settings, get_settings
from project_name.main import create_app


def get_settings_override() -> Settings:
    """テスト用設定を返す。"""
    return Settings(
        app_name="Test App",
        debug=True,
        environment="development",
        secret_key="test-secret-key-at-least-32-characters",
    )


@pytest.fixture
def app():
    """テスト用FastAPIアプリを提供する。"""
    app = create_app(settings=get_settings_override())
    app.dependency_overrides[get_settings] = get_settings_override
    return app


@pytest.fixture
def client(app) -> Generator[TestClient, None, None]:
    """同期テストクライアントを提供する。"""
    with TestClient(app) as client:
        yield client


@pytest.fixture
async def async_client(app) -> AsyncGenerator[AsyncClient, None]:
    """非同期テストクライアントを提供する。"""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client
```

### 10.2 APIテスト例

```python
"""APIエンドポイントのテスト。"""

from __future__ import annotations

import pytest
from fastapi import status
from fastapi.testclient import TestClient


class TestHealthEndpoints:
    """ヘルスチェックエンドポイントのテスト。"""

    def test_health_check(self, client: TestClient) -> None:
        """ヘルスチェックが正常に動作することを確認する。"""
        response = client.get("/health")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "healthy"

    def test_readiness_check(self, client: TestClient) -> None:
        """Readinessチェックが正常に動作することを確認する。"""
        response = client.get("/ready")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["status"] == "ready"


class TestUserEndpoints:
    """ユーザーエンドポイントのテスト。"""

    def test_create_user(self, client: TestClient) -> None:
        """ユーザー作成が正常に動作することを確認する。"""
        user_data = {
            "email": "test@example.com",
            "name": "Test User",
            "password": "securepassword123",
        }

        response = client.post("/api/v1/users/", json=user_data)

        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["email"] == user_data["email"]
        assert data["name"] == user_data["name"]
        assert "id" in data

    def test_create_user_invalid_email(self, client: TestClient) -> None:
        """無効なメールアドレスでエラーになることを確認する。"""
        user_data = {
            "email": "invalid-email",
            "name": "Test User",
            "password": "securepassword123",
        }

        response = client.post("/api/v1/users/", json=user_data)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
class TestAsyncEndpoints:
    """非同期テストの例。"""

    async def test_async_endpoint(self, async_client) -> None:
        """非同期クライアントでのテスト例。"""
        response = await async_client.get("/health")

        assert response.status_code == status.HTTP_200_OK
```

---

## 11. デプロイ

### 11.1 Docker

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
COPY alembic/ ./alembic/
COPY alembic.ini ./

# 非rootユーザーで実行
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# ポート公開
EXPOSE 8000

# ヘルスチェック
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 実行
CMD ["uv", "run", "uvicorn", "src.project_name.main:app", \
    "--host", "0.0.0.0", "--port", "8000"]
```

### 11.2 docker-compose.yml

```yaml
version: "3.8"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=production
      - DATABASE_URL=postgresql+asyncpg://user:password@db:5432/appdb
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: appdb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d appdb"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

### 11.3 本番実行コマンド

```bash
# Uvicorn（単一プロセス）
uvicorn src.project_name.main:app --host 0.0.0.0 --port 8000

# Uvicorn（複数ワーカー）
uvicorn src.project_name.main:app --host 0.0.0.0 --port 8000 --workers 4

# Gunicorn + Uvicorn（推奨）
gunicorn src.project_name.main:app \
    -w 4 \
    -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000
```

---

## 12. .gitignore への追加

汎用仕様書の`.gitignore`に以下を追加：

```gitignore
# FastAPI / Uvicorn
.env

# Alembic
alembic/versions/*.pyc

# SQLite（開発用）
*.db
*.sqlite3
```

---

## 13. セットアップ手順

```bash
# 1. 汎用仕様書のセットアップを実行後...

# 2. 環境変数設定
cp .env.example .env
# .env を編集

# 3. DBマイグレーション（使用する場合）
make migrate

# 4. 開発サーバー起動
make run

# 5. APIドキュメント確認
# http://localhost:8000/api/v1/docs (Swagger UI)
# http://localhost:8000/api/v1/redoc (ReDoc)
```

---

## 付録A: チェックリスト

### 新規プロジェクト作成時

- [ ] 汎用プロジェクト構造を作成
- [ ] `core/config.py` でPydantic Settingsを設定
- [ ] `.env.example` を作成
- [ ] `main.py` でアプリファクトリを実装
- [ ] ヘルスチェックエンドポイントを追加
- [ ] CORSミドルウェアを設定
- [ ] テストのセットアップ（conftest.py）
- [ ] Makefileに `run` ターゲットを追加

### デプロイ前

- [ ] `DEBUG=false` を確認
- [ ] `SECRET_KEY` が十分に長いことを確認
- [ ] CORS設定が適切か確認
- [ ] ヘルスチェックエンドポイントが機能するか確認
- [ ] DBマイグレーションが適用されているか確認

---

## 付録B: よく使うFastAPI API

| API | 用途 |
|-----|------|
| `FastAPI()` | アプリケーションインスタンス作成 |
| `APIRouter()` | ルーターグループ作成 |
| `Depends()` | 依存性注入 |
| `HTTPException` | HTTPエラーレスポンス |
| `status` | HTTPステータスコード定数 |
| `Body()`, `Query()`, `Path()` | パラメータ定義 |
| `Header()`, `Cookie()` | ヘッダー・クッキー取得 |
| `BackgroundTasks` | バックグラウンドタスク |
| `Response`, `JSONResponse` | カスタムレスポンス |

---

## 付録C: よく使うコマンド

| 用途 | コマンド |
|------|---------|
| 開発サーバー起動 | `make run` |
| 本番サーバー起動 | `make run-prod` |
| テスト実行 | `make test` |
| マイグレーション実行 | `make migrate` |
| マイグレーション作成 | `make migrate-new` |
| Swagger UI | http://localhost:8000/api/v1/docs |
| ReDoc | http://localhost:8000/api/v1/redoc |
| OpenAPI JSON | http://localhost:8000/api/v1/openapi.json |

---

**改訂履歴**

| バージョン | 日付 | 内容 |
|-----------|------|------|
| 1.0 | 2025-01 | 初版作成 |
