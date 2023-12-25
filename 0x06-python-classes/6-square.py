#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """The class defines a square using the its size
        Attributes:
            size (int): The size of the square to define
            position (:obj:`int`, optional): The position to start
                printing the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
         Args:
            size (int): The size of the square defines it and
                it plays a crucial part in the definition of the
                square so it needs to be controlled.
            position(:obj: `int`, optional): the position to start
                printing the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """(:obj:`int`): The tuple must be of size 2 and
                the elements must be integers otherwise
                an exception should be raised
        """

        return self.__position
    
    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
