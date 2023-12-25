#!/usr/bin/python3
"""This module conatins one function `load_from_file`
    this creates an object from JSON file
"""
import json


def load_from_json_file(filename):
    """The function loads a python object from a
        json file
    Args:
        filename (str): The filename
    Return:
        the python object
    """

    with open(filename, encoding="UTF8", mode='r') as f:
        python_obj = json.load(f)

    return python_obj
