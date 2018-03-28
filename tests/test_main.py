
from abvci.main import square


def test_zero():
    assert square(0) == 0


def test_positive_values():
    assert square(5) == 25
    assert square(1000) == 1000000


def test_negative_values():
    assert square(-5) == 25
    assert square(-1000) == 1000000
