import pytest


@pytest.mark.parametrize("role", ["admin", "user", "guest"])
@pytest.mark.parametrize("method", ["GET", "POST"])
def test_access(role, method):
    l1 = []
    role, method = role, method
    l1.append([role, method])
    for i in l1:
      print(i)
