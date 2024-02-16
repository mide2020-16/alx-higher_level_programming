#!/usr/bin/python3
"""
Function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int): First integer
        b (int): Second integer (default is 98)

    Returns:
        int: The addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
