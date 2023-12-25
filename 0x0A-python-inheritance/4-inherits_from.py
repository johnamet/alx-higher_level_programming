#!/usr/bin/python3
"""The module contains one function inherits from
    that checks if an obj is a subclass of a class
"""


def inherits_from(obj, a_class):
    """The function checks if an objects is a subclass
        of a class.
    Args:
        obj (obj): The object
        a_class (cls): the class
    Return:
        True if the object is a subclass otherwise False
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
