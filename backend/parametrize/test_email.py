import pytest

@pytest.mark.parametrize("email", ["a@b.com", "c@d.com", "e@f.com"])
def test_has_at(email):
    assert "@" in email
