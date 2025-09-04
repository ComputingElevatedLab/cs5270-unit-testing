import pytest
from math_utils import add, divide, fib

def test_add_simple():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide_normal_cases():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_fib_small_values():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(7) == 13

def test_fib_negative():
    with pytest.raises(ValueError):
        fib(-1)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (7, 13),
])
def test_fib_param(n, expected):
    assert fib(n) == expected
