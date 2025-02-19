# app/math_utils.py

import random

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def flaky_function(x):
    """A function that randomly fails to simulate flaky tests"""
    if random.random() < 0.3:  # 30% chance of failure
        raise RuntimeError("Random failure occurred!")
    return x * 2