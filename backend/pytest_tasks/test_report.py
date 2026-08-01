import pytest


runs = []

@pytest.fixture(scope='class')
def db():
    runs.append(1)
    print(len(runs))
    return {'ok': True}


class TestRepot:
    def test_one(self, db):
        assert db['ok'] == True

    def test_two(self, db):
        assert db['ok'] == True

    def test_three(self, db):
        assert db['ok'] == True
