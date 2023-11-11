#!/usr/bin/python3
"""This is a base model class"""


class Base:
    """This is a base class
    Attributes:
        nb_objects (int):m Number of objects

    Args:
        id (int): an id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
