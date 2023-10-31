#!/usr/bin/python3
"""This module prints a square"""


def print_square(size):
    """This function prints a square given its size
    
    Args:
        size (int): The size of the square


    >>> print_square(4) #doctest: +NORMALIZE_WHITESPACE
    ####
    ####
    ####
    ####

    >>> print_square("p")
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    >>> print_square(0.5)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    >>> print_square(-4)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0

    >>> print_square(0)


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("{}".format("#"*size))
