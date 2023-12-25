#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0

    is_error = False

    list_to_print = my_list[:x]

    while i < x:
        try:
            print("{:d}".format(list_to_print[i]), end="")
            i += 1
        except (TypeError, ValueError):
            i += 1
        else:
            count += 1
    print()

    return count
