# tests/test_math_utils.py

import pytest
import random
from app.math_utils import add, subtract, multiply, divide, flaky_function

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Flaky Tests (random failures)
def test_flaky_1():
    if random.random() < 0.3:  # 30% chance of failure
        assert False, "Flaky test 1 failed randomly"
    assert True

def test_flaky_2():
    if random.random() < 0.3:  # 30% chance of failure
        assert False, "Flaky test 2 failed randomly"
    assert True

def test_flaky_3():
    if random.random() < 0.3:  # 30% chance of failure
        assert False, "Flaky test 3 failed randomly"
    assert True

# Additional tests
def test_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_negative_numbers():
    assert subtract(-10, -5) == -5