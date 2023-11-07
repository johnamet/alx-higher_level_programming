#!/usr/bin/python3
"""The module contains one class BaseGeometry
    attributes:
"""


class BaseGeometry:
    """The base geometry is a class that performs
        simple geometry
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height

    def area(self):
        """The area method calculates the area of an object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if the value is an integer
            Args:
                name (str): The name (description) of the value
                value (int): The value to check
        """
        if not isinstance(type(value), int) and type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
