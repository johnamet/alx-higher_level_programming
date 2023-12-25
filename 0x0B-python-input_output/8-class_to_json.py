#!/usr/bin/python3
"""The module saves a class atrribute to json file"""


def class_to_json(obj):
    """The function takes a dict objct desc of a class
        and save it to a JSON file
    Args:
        obj (obj): the object
    """

    # create an empty dictionary to store the JSON representation
    json_dict = {}
    # iterate over the attributes and values of the object
    for key, value in obj.__dict__.items():
        # check the type of the value
        if isinstance(value, (list, dict, str, int, bool)):
            # if the value is a simple data structure, add it to the json_dict
            json_dict[key] = value
        elif isinstance(value, object):
            # if the value is another object,
            # recursively call the same function on it
            # and add the result to the json_dict
            json_dict[key] = class_to_json(value)
    # return the json_dict as the JSON representation of the object
    return json_dict
