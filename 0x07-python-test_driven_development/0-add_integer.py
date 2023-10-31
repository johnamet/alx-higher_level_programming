#!/usr/bin/python
"""The module add two integers"""


def add_integer(a, b=98):
    """The function adds two integers
    Args:
        a (int/float): First integer to add
        b (int/float): Second integer to add

    Returns: The sum of a and b
    """

    if not isinstance(a, (int,float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
