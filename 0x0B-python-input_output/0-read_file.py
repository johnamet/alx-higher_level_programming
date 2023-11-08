#!/usr/bin/python3
"""The module contains one function `read_file`, the function reads a text file and prints
    it out to stdout
"""


def read_file(filename=""):
    """The read_file function reads a file and prints it out to
        the stdout.
    Args:
        filename (str): the name of the file to read
    """

    with open(filename, encoding="UTF8", mode="r") as f:
        read_data = f.read()
        print(read_data, end="")
