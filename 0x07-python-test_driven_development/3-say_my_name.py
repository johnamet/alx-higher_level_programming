#!/usr/bin/python3
"""Prints full name"""


def say_my_name(first_name, last_name=""):
    """This function prints the fullname
    Args:
        first_name (str): the first name of the user
        last_name (str): the last name of the user

    Returns:
        Nothing

    >>> say_my_name("John", "Ametepe")
    My name is John Ametepe

    >>> say_my_name("John") #doctest: +NORMALIZE_WHITESPACE
    My name is John 

    >>> say_my_name(12)
    Traceback (most recent call last):
    TypeError: first_name must be a string

    >>> say_my_name("John", True)
    Traceback (most recent call last):
    TypeError: last_name must be a string

    >>> say_my_name(1, True)
    Traceback (most recent call last):
    TypeError: first_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
