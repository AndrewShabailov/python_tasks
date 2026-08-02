import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        if "wip" in item.keywords:
            item.add_marker(pytest.mark.skip(reason="still in progress"))
