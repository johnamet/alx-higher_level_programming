#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle:
    """This class defines a rectangle
    Attributes:
        width (int): The width if the rectangle
        height (int): The height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        rect = ""
        for i in range(self.height):
            rect += "{}".format("#" * self.width)
            if i < self.height - 1 and self.width != 0:
                rect += "\n"
        return rect