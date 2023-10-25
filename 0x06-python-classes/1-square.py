#!/usr/bin/python3
"""The module is defines a square
"""


class Square():
    """This class defines a square using its size

        Attributes:
            size (int): The size of the square to define
    """

    def __init__(self, size):
        """
        Args:
            size (int): The size of the square defines it and
                it plays a crucial part in the definition of the
                square so it needs to be controlled.
        """

        self.__size = size
