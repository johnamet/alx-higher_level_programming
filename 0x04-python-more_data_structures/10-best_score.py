#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    if len(a_dictionary) == 0:
        return None

    max_val = max(a_dictionary.values())

    max_key = [key for key in a_dictionary.keys()
                if a_dictionary[key] == max_val]

    return max_key[0]
