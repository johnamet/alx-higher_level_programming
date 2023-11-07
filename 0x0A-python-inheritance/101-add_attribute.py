#!/usr/bin/python3
"""The module contains one function that adds a new attribute to an object
    if possible
"""


def add_attribute(obj, name, value):
    """The function add attributes adds new attributes to an object
    Args:
        obj (:obj): The object
        name (str): the name of the attribute
        value (obj): the value of the object
    """

    if hasattr(obj, "__dict__"):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
