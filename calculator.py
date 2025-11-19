"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("Can't square negative numbers")

def hypotenuse(a ,b):
        return math.hypot(a,b)


def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    return b/a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Must be positive.")
    return math.log(b, a)

def exponent(a, b):
    return a**b
