#!/usr/bin/python3
"""The module contains one class BaseGeometry
    attributes:
"""


class BaseGeometry:
    """The base geometry is a class that performs
        simple geometry
    """

    def __init__(self):
        pass

    def area(self):
        """The area method calculates the area of an object"""
        raise NotImplementedError("area() is not implemented")
