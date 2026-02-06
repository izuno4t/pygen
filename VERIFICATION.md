# Verification

## plain

- `uv sync --dev` (pass)
- `uv sync --extra dev` (pass)
- `uv run ruff format .` (pass)
- `uv run ruff check .` (pass)
- `uv run mypy .` (pass)
- `uv run pytest` (pass)

## fastapi

- `uv sync --dev` (pass)
- `uv sync --extra dev` (pass)
- `uv run ruff format .` (pass)
- `uv run ruff check .` (pass)
- `uv run mypy .` (pass)
- `uv run pytest` (pass)

## streamlit

- `uv sync --dev` (pass)
- `uv sync --extra dev` (pass)
- `uv run ruff format .` (pass)
- `uv run ruff check .` (pass)
- `uv run mypy .` (pass)
- `uv run pytest` (pass)

## markdownlint

- `markdownlint-cli2 docs/PYTHON-FASTAPI-SPEC.md` (fail: 既存違反)
- `markdownlint-cli2 docs/PYTHON-STREAMLIT-SPEC.md` (fail: 既存違反)
