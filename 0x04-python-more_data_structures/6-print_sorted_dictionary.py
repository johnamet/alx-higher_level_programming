#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        a_dictionary = {}

    sorted_keys = sorted(a_dictionary.keys())

    tmp_dict = {key: a_dictionary[key] for key in sorted_keys}

    a_dictionary = tmp_dict

    print("".join("{}: {}\n".format(k,v) for k,v in a_dictionary.items()), end="")
