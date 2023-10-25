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
        self.__size = size

    @property
    def size(self):
        """:int: The size must be greater than or equal to
                zero and must also be an integer
        """

        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 0

        while i != self.__size:
            j = 0

            while j != self.__size:
                print("#", end="")
                j += 1

            i += 1
            print()
