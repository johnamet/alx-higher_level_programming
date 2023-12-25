#!/usr/bin/python3
"""The module contains one function 'to json_string'
    it serialiazes an object to a json string
"""
import json


def to_json_string(my_obj):
    """The function serializes an obj
        to a json string
    Args:
        my_obj (obj): the object to serialize
    """

    return json.dumps(my_obj)
