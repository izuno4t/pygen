"""Integration smoke tests."""

def test_app_importable() -> None:
    import project_name.app  # noqa: F401
