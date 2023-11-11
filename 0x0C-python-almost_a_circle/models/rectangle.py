#!/usr/bin/python3
"""This module contains the rectangle class. The class defines a Rectangle
    in terms of area
"""
from models.base import Base


class Rectangle(Base):
    """This is a rectangle class
    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x-coordinate of the rectangle
        y (int): y-coordinate of the rectangle
        id (int): id of the rectangle

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x-coordinate of the rectangle
        y (int): y-coordinate of the rectangle
        id (int): id of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """Defines the area of a rectangle
            area = width * height
        """

        area = self.__width * self.__height
        return area

    def display(self):
        """The method displays the rectangle using `#` characters
            considering the x and y coordinates.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print("{}".format(" " * self.__x + "#" * self.__width))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                self.__width, self.__height)
