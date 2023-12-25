#!/usr/bin/python3
"""The module contains one class that checks if an object
    is a kind of class
"""


def is_kind_of_class(obj, a_class):
    """The function checks whether an object is an instance
        of a class
    Args:
        obj (object): The object
        a_class (:cls): The class
    Return:
        True if is an object of the class otherwise False
    """

    return isinstance(obj, a_class)
