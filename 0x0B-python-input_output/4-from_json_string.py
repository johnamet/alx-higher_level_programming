#!/usr/bin/python3
"""The module contains one function `from_json_string`
    that loads a json to a string
"""
import json


def from_json_string(my_str):
    """the function converts a json to a string
    Args:
        my_str (str): json string
    """

    obj = json.loads(my_str)

    return obj
