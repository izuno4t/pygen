"""pytest fixtures."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from fastapi.testclient import TestClient

from project_name.main import create_app


if TYPE_CHECKING:
    from collections.abc import Generator

    from fastapi import FastAPI


@pytest.fixture
def app() -> FastAPI:
    return create_app()


@pytest.fixture
def client(app: FastAPI) -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client
