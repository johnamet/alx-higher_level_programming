#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        list_to_print = my_list[:x]
    except IndexError:
        return 0

    for e in list_to_print:
        count += 1
        print("{}".format(e), end="")

    print()

    return count
