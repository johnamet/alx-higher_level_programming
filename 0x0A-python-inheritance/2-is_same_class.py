#!/usr/bin/python3
"""This module contains one function `is_same_class`
    it checks whether an object is exactly an instance
    of a class
"""


def is_same_class(obj, a_class):
    """The function checks if an object is an instance
        of a class.
        Args:
            obj (:object): The object
            a_class (object): The class
        Returns:
            :bool - True if it is an instance otherwise False
    """

    return type(obj) is a_class
