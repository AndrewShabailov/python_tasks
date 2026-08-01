import pytest

@pytest.mark.skip(reason= "fixed in new version")
def test_dashboard():
    assert False

@pytest.mark.xfail(reason= "bug #21")
def test_export():
    assert 2 + 2 == 5

@pytest.mark.xpassed(reason= "works as expected")
def test_import():
    assert 2 + 2 == 4
