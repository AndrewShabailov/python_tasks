import pytest


order = []


@pytest.fixture(scope="module", autouse=True)
def module_setup():
    order.append('module setup')
    yield
    order.append('module teardown')
    print(order)

@pytest.fixture
def func_fixture():
    order.append('func setup')
    yield
    order.append('func teardown')


def test_demo(func_fixture):
    order.append('test body')
    assert True
