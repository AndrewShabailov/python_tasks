import pytest
import sys


@pytest.mark.skip
def test_skip_this():
    assert False

@pytest.mark.skipif(sys.platform == 'win32', reason='not for windows')
def test_not_on_windows():
    pass

@pytest.mark.xfail(reason= 'Bug #22 is not fixed yet')
def test_buggy():
    assert 1 == 2

@pytest.mark.parametrize('num', [1, 2, 3])
def test_nums(num):
    assert num < 5
    