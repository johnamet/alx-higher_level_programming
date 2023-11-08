#!/usr/bin/python3
"""This module contains one function 'write_file'
    that writes a text to file
"""


def write_file(filename="", text=""):
    """The function writes a text to a file
    Args:
        filename (str): The name of the file
        text (str): The text to wriye
    """

    with open(filename, encoding="UTF8", mode="w") as f:
        f.write(text)

    return len(text)
