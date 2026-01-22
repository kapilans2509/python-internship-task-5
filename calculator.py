# Task 5: Functions & Modular Programming
# Modular Calculator Program

def add(a, b=0):
    """
    Returns the sum of two numbers.
    Default value for b is 0.
    """
    return a + b


def subtract(a, b):
    """
    Returns the difference of two numbers.
    """
    return a - b


def multiply(a, b):
    """
    Returns the product of two numbers.
    """
    return a * b


def divide(a, b):
    """
    Returns the division of two numbers.
    Handles division by zero.
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


# ------------------ Testing Functions ------------------

print("Addition:", add(10, 5))
print("Addition with default argument:", add(10))

print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Division by zero:", divide(10, 0))
