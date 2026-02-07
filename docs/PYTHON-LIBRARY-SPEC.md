# Python ライブラリ仕様書

**作成日**: 2025年1月  
**対象**: Python 3.11+  
**想定用途**: PyPI 公開を前提としたライブラリ開発

---

## 1. 概要

### 1.1 目的

PyPI 公開を前提に、以下を満たす Python ライブラリの最小構成を定義する。

- **配布性**: `pyproject.toml` によるメタデータ管理
- **保守性**: `src` レイアウトの採用
- **品質**: `ruff` / `mypy` / `pytest` による品質維持

---

## 2. プロジェクト構造

```text
library/
├── src/
│   └── project_name/
│       └── __init__.py
├── tests/
│   └── test_basic.py
├── .pre-commit-config.yaml
├── .python-version
├── Makefile
├── pyproject.toml
└── README.md
```

---

## 3. pyproject.toml

### 3.1 必須メタデータ

```toml
[project]
name = "project-name"
version = "0.1.0"
description = "Library description"
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.11"
authors = [
    { name = "Author Name", email = "author@example.com" }
]
keywords = ["keyword1", "keyword2"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13"
]
```

### 3.2 依存関係

```toml
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=4.0",
    "mypy>=1.8",
    "ruff>=0.4",
    "pre-commit>=3.6",
    "taplo>=0.9.3"
]
```

### 3.3 ビルド設定

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/project_name"]
```

---

## 4. 設定ポリシー

- **Ruff / mypy / pytest** を `pyproject.toml` に集約
- **pre-commit** で自動チェックを標準化
- **Makefile** に開発コマンドを集約

---

## 5. Makefile

```makefile
.PHONY: help install dev test lint format typecheck check clean

help:
    @printf "\033[36m✨ Available commands:\033[0m\n"
    @echo "  make install    - Install production dependencies"
    @echo "  make dev        - Install all dependencies (including dev)"
    @echo "  make test       - Run tests"
    @echo "  make lint       - Run linter"
    @echo "  make format     - Format code"
    @echo "  make typecheck  - Run type checker"
    @echo "  make check      - Run all checks (lint, typecheck, test)"
    @echo "  make clean      - Remove build artifacts"

install:
    uv sync

dev:
    uv sync --extra dev
    uv run pre-commit install

test:
    uv run pytest

lint:
    uv run ruff check .

format:
    uv run ruff format .
    uv run ruff check --fix .

typecheck:
    uv run mypy .

check: lint typecheck test

clean:
    rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
```

---

## 6. セットアップ

```bash
uv sync --extra dev
uv run pre-commit install
```

---

## 7. CI（任意）

CIを導入する場合の基本チェックは以下を推奨する。

- `make lint`
- `make format`
- `make typecheck`
- `make test`

TOMLが変更された場合は以下も実行する。

- `make taplo`

---

## 改訂履歴

| バージョン | 日付 | 内容 |
| --- | --- | --- |
| 1.0 | 2025-01 | 初版作成 |
