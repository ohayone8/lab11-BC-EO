"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

# raise ZeroDivisionError if a == 0
def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b/a

# use math library + raise ValueError
def log(a, b):
    if b<=0:
        raise ValueError
    math.log(b, a)

def exp(a, b):
    return a**b
import math

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Must be positive.")
    return math.log(b, a)

def exponent(a, b):
    return a**b
