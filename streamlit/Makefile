.PHONY: help install dev test lint format typecheck check clean run run-dev

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

install:
	uv sync

dev:
	uv sync --dev
	uv run pre-commit install
	@echo "Don't forget to copy .streamlit/secrets.toml.example to .streamlit/secrets.toml"

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

run:
	uv run streamlit run src/project_name/app.py

run-dev:
	uv run streamlit run src/project_name/app.py --server.runOnSave=true

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
