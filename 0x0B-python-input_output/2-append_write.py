#!/usr/bin/python3
"""This module contains one function 'write_file'
    that writes/append  a text to file
"""


def append_write(filename="", text=""):
    """The function write/appends a text to a file
    Args:
        filename (str): The name of the file
        text (str): The text to wriye
    """

    with open(filename, encoding="UTF8", mode="a") as f:
        f.write(text)

    return len(text)
