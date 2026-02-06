"""CLI entry points."""

from __future__ import annotations

import uvicorn


def dev() -> None:
    """Run development server."""
    uvicorn.run(
        "project_name.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
