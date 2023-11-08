#!/usr/bin/python3
"""The module contains one function `save_to_json`
"""
import json


def save_to_json_file(my_obj, filename):
    """The function saves a python object to a
        json
    Args:
        my_obj (obj): The python object
        filename (str): The filename of the file
    """

    with open(filename, encoding='UTF8', mode='w') as f:
        json.dump(my_obj, f)
