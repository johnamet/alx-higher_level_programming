#!/usr/bin/python3
"""This is a base model class"""
import json


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

    def to_json_string(list_dictionaries):
        """The method returns json representation of
            list dictionaries
        Args:
            list_dictionaries (obj): is a list of dictionaries
        """
        if not list_dictionaries and len(list_dictionaries) == 0:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)

        return json_str
