"""Main entry point tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

from project_name import __main__


if TYPE_CHECKING:
    from pytest import CaptureFixture


def test_main_prints(capsys: CaptureFixture[str]) -> None:
    __main__.main()
    captured = capsys.readouterr()
    assert "project-name" in captured.out
