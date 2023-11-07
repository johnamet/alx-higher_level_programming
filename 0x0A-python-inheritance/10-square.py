#!/usr/bin/python3
"""The module has one class `Square` that inherits from
    the Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class inherits from the rectangle class
    """

    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """The method computes the area of a square"""
        return self.__size ** 2
