#!/usr/bin/python3
"""The module contains one function that prints the
    attributes and methods of a class
"""


def lookup(obj):
    """The function returns the list of available attributes
        and methods of an object.
    Args:
        obj (:object): the object to list attributes

    Returns:
        The attributes and methods of an object
    """

    return dir(obj)
