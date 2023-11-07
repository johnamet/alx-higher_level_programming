#!/usr/bin/python3
"""The module contains one class Rectangle that inherits
    from the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The rectangle class inherits from the BasGeometry class
    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """

    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
