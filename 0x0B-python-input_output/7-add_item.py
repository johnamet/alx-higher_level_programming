#!/usr/bin/python3
"""The script that adds all arguments to a python list,
    and save them to a file
"""
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main(*args):
    """The main function
    Args:
        args (obj): arguments from the command line
    """

    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(args[1:])
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    import sys
    main(*sys.argv)
