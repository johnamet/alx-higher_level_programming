#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return a_dictionary

    a_dictionary = {i: a_dictionary[i]*2 for i in a_dictionary.keys()}

    return a_dictionary
