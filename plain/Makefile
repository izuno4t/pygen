.PHONY: help install dev test test-cov lint format typecheck check clean run

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
	@echo "  make run        - Run application"
	@echo "  make clean      - Remove build artifacts"

install:
	uv sync

dev:
	uv sync --dev
	uv run pre-commit install

test:
	uv run pytest

test-cov:
	uv run pytest --cov --cov-report=html --cov-report=term-missing

lint:
	uv run ruff check .

format:
	uv run ruff format .
	uv run ruff check --fix .

typecheck:
	uv run mypy .

check: lint typecheck test

run:
	@MODULE="$$(python - <<'PY'\nfrom __future__ import annotations\n\nfrom pathlib import Path\nimport tomllib\n\npyproject = Path(\"pyproject.toml\")\nif not pyproject.exists():\n    raise SystemExit(\"pyproject.toml not found\")\n\ndata = tomllib.loads(pyproject.read_text(encoding=\"utf-8\"))\nname = data.get(\"project\", {}).get(\"name\")\nif not name:\n    raise SystemExit(\"project.name not found in pyproject.toml\")\n\nprint(name.replace(\"-\", \"_\"))\nPY\n)"; \\\n\tuv run python -m "$$MODULE"

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
