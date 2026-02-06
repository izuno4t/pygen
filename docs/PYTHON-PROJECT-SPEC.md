# Python Webアプリケーション ボイラープレート仕様書

## 汎用プロジェクトスタイル編（フレームワーク非依存）

**作成日**: 2025年1月  
**対象**: Python 3.11+ / 3.12+ 推奨  
**想定用途**: StreamlitおよびFastAPIアプリケーションの共通基盤

---

## 1. 概要

### 1.1 本仕様書の目的

2024-2025年におけるPython開発のベストプラクティスに基づき、以下を実現するボイラープレートの仕様を定義する。

- **一貫性**: 統一されたコードスタイルと構造
- **保守性**: 長期運用に耐える設計
- **効率性**: 高速な開発サイクル（リント・テスト・ビルド）
- **安全性**: 型チェックと自動品質検査

### 1.2 技術スタック選定理由

| カテゴリ | 採用ツール | 選定理由 |
| --- | --- | --- |
| パッケージ管理 | **uv** | pip比10-100倍高速、Rustベース、オールインワン |
| リンター/フォーマッター | **Ruff** | Flake8+Black+isort置換、超高速、単一ツール |
| 型チェッカー | **mypy** | デファクトスタンダード、厳格な型検査 |
| テストフレームワーク | **pytest** | 柔軟性、豊富なプラグイン、簡潔な記法 |
| pre-commitフック | **pre-commit** | 自動品質保証、CI統合 |
| CI/CD | 任意（GitHub Actions, GitLab CI等） | プロジェクトに応じて選択 |

---

## 2. プロジェクト構造

### 2.1 推奨レイアウト: src layout

**選定理由**: 本番環境向けアプリケーションには`src`レイアウトを推奨

- インポートの曖昧性を排除（開発中コードとインストール済みパッケージの混同防止）
- テストが常にインストール済みパッケージに対して実行される
- 配布物に不要なファイル（README、設定ファイル等）が含まれない

### 2.2 ディレクトリ構造

```text
project-name/
├── .devcontainer/                 # Dev Container設定（オプション）
│   ├── devcontainer.json
│   └── Dockerfile                 # カスタムイメージ使用時
├── src/
│   └── project_name/              # メインパッケージ（ハイフン→アンダースコア）
│       ├── __init__.py
│       ├── __main__.py            # python -m project_name 用エントリポイント
│       ├── py.typed               # PEP 561 型情報マーカー
│       ├── core/                  # ビジネスロジック
│       │   ├── __init__.py
│       │   └── ...
│       ├── domain/                # ドメインモデル
│       │   ├── __init__.py
│       │   └── ...
│       ├── infrastructure/        # 外部サービス連携
│       │   ├── __init__.py
│       │   └── ...
│       └── utils/                 # ユーティリティ
│           ├── __init__.py
│           └── ...
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # pytest共通フィクスチャ
│   ├── unit/                      # ユニットテスト
│   │   └── ...
│   └── integration/               # 統合テスト
│       └── ...
├── docs/                          # ドキュメント（オプション）
│   └── ...
├── scripts/                       # 開発用スクリプト（オプション）
│   └── ...
├── .env.example                   # 環境変数テンプレート（.envはgitignore）
├── .gitignore
├── .pre-commit-config.yaml        # pre-commit設定
├── .python-version                # Pythonバージョン指定（pyenv/uv用）
├── Makefile                       # 開発コマンドショートカット
├── pyproject.toml                 # プロジェクト設定（単一ファイルに集約）
├── uv.lock                        # 依存関係ロックファイル（自動生成）
├── README.md
└── LICENSE
```

### 2.3 命名規則

| 対象 | 規則 | 例 |
| --- | --- | --- |
| プロジェクト名 | ケバブケース | `my-awesome-app` |
| パッケージ名 | スネークケース | `my_awesome_app` |
| モジュール名 | スネークケース | `data_loader.py` |
| クラス名 | パスカルケース | `DataLoader` |
| 関数/変数名 | スネークケース | `load_data()` |
| 定数名 | アッパースネークケース | `MAX_RETRY_COUNT` |

---

## 3. pyproject.toml 設定

### 3.1 基本構成

```toml
[project]
name = "project-name"
version = "0.1.0"
description = "プロジェクトの説明"
readme = "README.md"
license = "MIT"
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
    "Programming Language :: Python :: 3.13",
]

dependencies = [
    # 本番依存関係をここに記載
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=4.0",
    "pytest-asyncio>=0.23",
    "mypy>=1.8",
    "ruff>=0.4",
    "pre-commit>=3.6",
]

[project.urls]
Homepage = "https://github.com/username/project-name"
Documentation = "https://project-name.readthedocs.io"
Repository = "https://github.com/username/project-name"
Issues = "https://github.com/username/project-name/issues"

[project.scripts]
# CLIエントリポイント（必要な場合）
project-name = "project_name.__main__:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/project_name"]
```

### 3.2 Ruff設定

```toml
[tool.ruff]
target-version = "py311"
line-length = 88
indent-width = 4

# src layoutの場合
src = ["src", "tests"]

# 除外パターン
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
]

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # Pyflakes
    "I",      # isort
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "UP",     # pyupgrade
    "ARG",    # flake8-unused-arguments
    "SIM",    # flake8-simplify
    "TCH",    # flake8-type-checking
    "PTH",    # flake8-use-pathlib
    "ERA",    # eradicate (commented-out code)
    "PL",     # Pylint
    "RUF",    # Ruff-specific rules
]

ignore = [
    "E501",   # line too long (formatterに任せる)
    "B008",   # function call in default argument (FastAPI Depends対応)
    "PLR0913", # too many arguments
]

# 自動修正可能なルール
fixable = ["ALL"]
unfixable = []

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = [
    "S101",   # assert使用許可
    "ARG",    # 未使用引数許可（フィクスチャ）
    "PLR2004", # マジックナンバー許可
]

[tool.ruff.lint.isort]
known-first-party = ["project_name"]
force-single-line = false
lines-after-imports = 2

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
docstring-code-format = true
docstring-code-line-length = "dynamic"
```

> NOTE: `tool.ruff.lint` 形式はRuffの正しい設定だが、TOML拡張のスキーマが古い場合にエディタ側でエラー表示されることがある。Ruffのスキーマに更新するか、該当警告を無視する設定を行う。

### 3.3 mypy設定

```toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
show_error_codes = true
show_column_numbers = true

# src layoutの場合
mypy_path = "src"
packages = ["project_name"]

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false

[[tool.mypy.overrides]]
# サードパーティで型スタブがないモジュール
module = [
    "some_untyped_library.*",
]
ignore_missing_imports = true
```

### 3.4 pytest設定

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "-v",
    "-ra",
    "--strict-markers",
    "--strict-config",
    "--tb=short",
    "--cov=src/project_name",
    "--cov-report=term-missing",
    "--cov-report=html:htmlcov",
    "--cov-fail-under=80",
]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
]
filterwarnings = [
    "error",
    "ignore::DeprecationWarning",
]
asyncio_mode = "auto"
```

### 3.5 coverage設定

```toml
[tool.coverage.run]
source = ["src"]
branch = true
omit = [
    "*/tests/*",
    "*/__main__.py",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "@abstractmethod",
]
show_missing = true
```

---

## 4. 開発ツール設定

### 4.1 pre-commit設定 (`.pre-commit-config.yaml`)

```yaml
default_language_version:
  python: python3.11

repos:
  # 汎用フック
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
        args: [--unsafe]
      - id: check-toml
      - id: check-json
      - id: check-added-large-files
        args: [--maxkb=1000]
      - id: check-merge-conflict
      - id: detect-private-key
      - id: debug-statements
      - id: check-case-conflict

  # Ruff（リント＆フォーマット）
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.10
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  # mypy（型チェック）
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy
        additional_dependencies:
          # プロジェクトの依存関係に合わせて追加
          - types-requests
        args: [--config-file=pyproject.toml]

  # セキュリティチェック
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.9
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

ci:
  autofix_commit_msg: "style: auto-fix by pre-commit hooks"
  autoupdate_commit_msg: "chore: update pre-commit hooks"
```

### 4.2 bandit設定（pyproject.tomlに追加）

```toml
[tool.bandit]
exclude_dirs = ["tests", "docs"]
skips = ["B101"]  # assert使用を許可
```

### 4.3 CI/CD 設定（共通要件）

CI/CDツール（GitHub Actions, GitLab CI, CircleCI等）で以下のジョブを実行する：

#### 必須ジョブ

```yaml
# 疑似コード（各CIツールの記法に変換）

jobs:
  lint:
    # Ruffによるリント＆フォーマットチェック
    steps:
      - uv sync --dev
      - uv run ruff check .
      - uv run ruff format --check .
      - uv run mypy .

  test:
    # 複数Pythonバージョンでテスト
    matrix:
      python: ["3.11", "3.12", "3.13"]
    steps:
      - uv python install $python
      - uv sync --dev
      - uv run pytest --cov-report=xml

  security:
    # セキュリティチェック
    steps:
      - uv sync --dev
      - uv run bandit -c pyproject.toml -r src/
```

#### CIで実行すべきコマンド一覧

| チェック項目 | コマンド |
| --- | --- |
| リントチェック | `uv run ruff check .` |
| フォーマットチェック | `uv run ruff format --check .` |
| 型チェック | `uv run mypy .` |
| テスト実行 | `uv run pytest` |
| カバレッジ付きテスト | `uv run pytest --cov --cov-report=xml` |
| セキュリティチェック | `uv run bandit -c pyproject.toml -r src/` |

### 4.4 Dev Container設定（オプション）

チーム開発や環境統一が必要な場合に使用。VSCode、PyCharm、GitHub Codespacesで利用可能。

#### `.devcontainer/devcontainer.json`

```json
{
  "name": "Python Development",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",

  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },

  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "charliermarsh.ruff",
        "ms-python.mypy-type-checker",
        "tamasfe.even-better-toml"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "[python]": {
          "editor.defaultFormatter": "charliermarsh.ruff",
          "editor.formatOnSave": true,
          "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
          }
        }
      }
    }
  },

  "postCreateCommand": "uv sync --dev && uv run pre-commit install",

  "remoteUser": "vscode"
}
```

#### カスタムDockerfile使用時

`.devcontainer/Dockerfile`:

```dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.11

# uv インストール
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# 追加パッケージ（必要に応じて）
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*
```

`.devcontainer/devcontainer.json`（Dockerfile参照版）:

```json
{
  "name": "Python Development",
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "postCreateCommand": "uv sync --dev && uv run pre-commit install",
  "remoteUser": "vscode"
}
```

#### Dev Containerのメリット

| メリット | 説明 |
| --- | --- |
| 環境統一 | 「自分のマシンでは動く」問題を完全解消 |
| 高速オンボーディング | clone → VSCodeで開く → 即開発可能 |
| ローカル環境クリーン | Python/依存関係は全てコンテナ内 |
| GitHub Codespaces対応 | ブラウザのみで開発可能 |

### 4.5 Makefile

よく使うコマンドのショートカット集。`make test` のように短いコマンドで実行できる。

```makefile
.PHONY: help install dev test test-cov lint format typecheck check clean

# デフォルトターゲット: ヘルプ表示
help:
    @echo "Available commands:"
    @echo "  make install    - Install production dependencies"
    @echo "  make dev        - Install all dependencies (including dev)"
    @echo "  make test       - Run tests"
    @echo "  make test-cov   - Run tests with coverage"
    @echo "  make lint       - Run linter"
    @echo "  make format     - Format code"
    @echo "  make typecheck  - Run type checker"
    @echo "  make check      - Run all checks (lint, typecheck, test)"
    @echo "  make clean      - Remove build artifacts"

# 依存関係インストール
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

# 全チェック実行
check: lint typecheck test

# クリーンアップ
clean:
    rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
```

#### Makefileのメリット

| メリット | 説明 |
| --- | --- |
| コマンド短縮 | `uv run pytest --cov...` → `make test-cov` |
| 自己文書化 | `make help` で使えるコマンド一覧表示 |
| CI/CDと統一 | ローカルもCIも同じコマンドで実行 |
| 新メンバー対応 | READMEに「`make dev`で環境構築」と書くだけ |

---

## 5. 依存関係管理

### 5.1 uvによるプロジェクト管理

```bash
# プロジェクト初期化（src layout）
uv init --package project-name
cd project-name

# 依存関係追加
uv add fastapi uvicorn  # 本番依存
uv add --dev pytest ruff mypy  # 開発依存

# 仮想環境同期
uv sync

# コマンド実行
uv run python -m project_name
uv run pytest

# ロックファイル更新
uv lock --upgrade
```

### 5.2 依存関係のグループ化

```toml
[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=4.0",
    "mypy>=1.8",
    "ruff>=0.4",
    "pre-commit>=3.6",
]
docs = [
    "mkdocs>=1.5",
    "mkdocs-material>=9.5",
    "mkdocstrings[python]>=0.24",
]
```

---

## 6. コーディング規約

### 6.1 型ヒント

```python
from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    from pathlib import Path

T = TypeVar("T")


def process_items(items: Sequence[T], callback: Callable[[T], None]) -> list[T]:
    """アイテムを処理する。

    Args:
        items: 処理対象のアイテムシーケンス
        callback: 各アイテムに適用するコールバック関数

    Returns:
        処理済みアイテムのリスト
    """
    result: list[T] = []
    for item in items:
        callback(item)
        result.append(item)
    return result
```

### 6.2 docstring形式（Google Style）

```python
def fetch_data(url: str, timeout: float = 30.0) -> dict[str, Any]:
    """指定URLからデータを取得する。

    Args:
        url: データ取得先のURL
        timeout: タイムアウト秒数。デフォルトは30秒。

    Returns:
        取得したデータを含む辞書

    Raises:
        ValueError: URLが不正な場合
        TimeoutError: タイムアウトした場合

    Example:
        >>> data = fetch_data("https://api.example.com/data")
        >>> print(data["status"])
        'ok'
    """
    pass
```

### 6.3 インポート順序（Ruffで自動整形）

```python
# 1. 標準ライブラリ
from __future__ import annotations

import json
import logging
from collections.abc import Sequence
from pathlib import Path

# 2. サードパーティ
import httpx
from pydantic import BaseModel

# 3. ローカル（自プロジェクト）
from project_name.core import processor
from project_name.utils.helpers import format_date
```

---

## 7. テスト規約

### 7.1 テストファイル構成

```text
tests/
├── __init__.py
├── conftest.py          # 共通フィクスチャ
├── unit/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
└── integration/
    ├── __init__.py
    └── test_api.py
```

### 7.2 テストの書き方

```python
"""ユニットテストのサンプル。"""

from __future__ import annotations

import pytest

from project_name.core.calculator import Calculator


class TestCalculator:
    """Calculatorクラスのテスト。"""

    @pytest.fixture
    def calculator(self) -> Calculator:
        """Calculatorインスタンスを提供する。"""
        return Calculator()

    def test_add_positive_numbers(self, calculator: Calculator) -> None:
        """正の数の加算をテストする。"""
        result = calculator.add(2, 3)
        assert result == 5

    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (1, 1, 2),
            (0, 0, 0),
            (-1, 1, 0),
            (100, 200, 300),
        ],
    )
    def test_add_various_numbers(
        self,
        calculator: Calculator,
        a: int,
        b: int,
        expected: int,
    ) -> None:
        """様々な数値の組み合わせで加算をテストする。"""
        assert calculator.add(a, b) == expected

    def test_divide_by_zero_raises_error(self, calculator: Calculator) -> None:
        """ゼロ除算でエラーが発生することをテストする。"""
        with pytest.raises(ZeroDivisionError):
            calculator.divide(10, 0)
```

### 7.3 conftest.py サンプル

```python
"""pytest共通フィクスチャ。"""

from __future__ import annotations

from collections.abc import AsyncGenerator, Generator
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def sample_data_dir(tmp_path: Path) -> Path:
    """テスト用の一時データディレクトリを提供する。"""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture
def mock_config() -> dict[str, str]:
    """テスト用の設定辞書を提供する。"""
    return {
        "api_url": "https://api.test.example.com",
        "timeout": "30",
    }


@pytest.fixture
async def async_client() -> AsyncGenerator[None, None]:
    """非同期クライアントのフィクスチャ例。"""
    # セットアップ
    yield
    # ティアダウン
```

---

## 8. Git設定

### 8.1 .gitignore

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.venv/
venv/
ENV/
env/

# uv
.python-version
uv.lock

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# Environments
.env
.env.local
*.env

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Ruff
.ruff_cache/

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
logs/
*.log
```

### 8.2 .python-version

```text
3.11
```

---

## 9. セットアップ手順

### 9.1 新規プロジェクト作成

```bash
# 1. uvのインストール（未インストールの場合）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. プロジェクト作成
uv init --package my-project
cd my-project

# 3. ディレクトリ構造の調整
mkdir -p src/my_project/{core,domain,infrastructure,utils}
mkdir -p tests/{unit,integration}
touch src/my_project/py.typed
touch src/my_project/__main__.py
touch tests/__init__.py tests/conftest.py

# 4. 開発依存関係の追加
uv add --dev pytest pytest-cov pytest-asyncio mypy ruff pre-commit bandit

# 5. pre-commitの設定
uv run pre-commit install
uv run pre-commit run --all-files

# 6. 初回テスト実行
uv run pytest
```

### 9.2 既存プロジェクトへの適用

```bash
# 1. pyproject.tomlの更新
# 本仕様書のテンプレートを参考に設定を追加

# 2. 依存関係の同期
uv sync

# 3. pre-commitフックのインストール
uv run pre-commit install

# 4. 全ファイルに対してリント実行
uv run ruff check --fix .
uv run ruff format .

# 5. 型チェック
uv run mypy .
```

### 9.3 Makefileを使う場合

```bash
# 開発環境セットアップ（依存関係インストール + pre-commit設定）
make dev

# 全チェック実行
make check

# または個別に
make lint
make format
make test
```

---

## 10. 今後の拡張（フレームワーク別）

本仕様書で定義した汎用プロジェクトスタイルを基盤として、以下のフレームワーク固有の設定を追加する：

### Streamlit向け拡張

- `src/project_name/app/` ディレクトリ構成
- ページルーティング設定
- セッション状態管理パターン
- 環境変数・シークレット管理

### FastAPI向け拡張

- `src/project_name/api/` ディレクトリ構成（routers, schemas, dependencies）
- Pydantic v2設定
- 非同期データベース接続パターン
- OpenAPI/Swagger設定
- ミドルウェア・CORS設定

---

## 付録A: 推奨VSCode設定

### settings.json

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    }
  },
  "python.analysis.typeCheckingMode": "basic",
  "ruff.lint.args": ["--config=pyproject.toml"],
  "ruff.format.args": ["--config=pyproject.toml"],
  "mypy-type-checker.args": ["--config-file=pyproject.toml"]
}
```

### extensions.json

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "charliermarsh.ruff",
    "ms-python.mypy-type-checker",
    "tamasfe.even-better-toml",
    "github.copilot"
  ]
}
```

---

## 付録B: よく使うコマンド一覧

### uvコマンド（直接実行）

| 用途 | コマンド |
| --- | --- |
| 依存関係追加 | `uv add <package>` |
| 開発依存追加 | `uv add --dev <package>` |
| 依存関係同期 | `uv sync` |
| テスト実行 | `uv run pytest` |
| カバレッジ付きテスト | `uv run pytest --cov` |
| リントチェック | `uv run ruff check .` |
| リント自動修正 | `uv run ruff check --fix .` |
| フォーマット | `uv run ruff format .` |
| 型チェック | `uv run mypy .` |
| pre-commit実行 | `uv run pre-commit run --all-files` |
| アプリ実行 | `uv run python -m project_name` |

### Makeコマンド（ショートカット）

| 用途 | コマンド |
| --- | --- |
| ヘルプ表示 | `make help` |
| 開発環境セットアップ | `make dev` |
| テスト実行 | `make test` |
| カバレッジ付きテスト | `make test-cov` |
| リントチェック | `make lint` |
| フォーマット | `make format` |
| 型チェック | `make typecheck` |
| 全チェック実行 | `make check` |
| クリーンアップ | `make clean` |

---

## 改訂履歴

| バージョン | 日付 | 内容 |
| --- | --- | --- |
| 1.0 | 2025-01 | 初版作成 |
| 1.1 | 2025-01 | Makefile追加、.env.example追加、Dev Container設定追加、CI/CD設定を汎用化 |
