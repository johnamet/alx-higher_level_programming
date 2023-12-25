#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """The class defines a square using the its size
        Attributes:
            size (int): The size of the square to define
    """

    def __init__(self, size=0):
        """
         Args:
            size (int): The size of the square defines it and
                it plays a crucial part in the definition of the
                square so it needs to be controlled.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
