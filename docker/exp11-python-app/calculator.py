"""Calculator utilities used by the CDD continuous-integration lab.

Author: Rizwan Shariff S M (4NI25CS163)
Course: 1BCS303 - Collaborative Development and DevOps
"""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print(f"Add(10, 5)      = {add(10, 5)}")
    print(f"Subtract(10, 5) = {subtract(10, 5)}")
    print(f"Multiply(10, 5) = {multiply(10, 5)}")
    print(f"Divide(10, 5)   = {divide(10, 5)}")
