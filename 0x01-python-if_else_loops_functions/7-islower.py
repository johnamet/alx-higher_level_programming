#!/usr/bin/python3
def islower(c):
    is_lower = ord(c) >= 97 and ord(c) < 123

    if (is_lower):
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
    return ord(c) >= 97 and ord(c) < 123
