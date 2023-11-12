#!/usr/bin/python3
"""This module describes a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class defines a square
    Attributes:
        size (int): The size of the square
        x (int): The x position of the square
        y (int): The y position of the square

    Args:
        size (int): The size of the square
        x (int): The x position of the square
        y (int): The y position of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width nust be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value
        self.width = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width)
