#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as e:
        sys.stderr.write(str(e)+"\n")
        return False
    except TypeError as te:
        sys.stderr.write(str(te)+"\n")
        return False

    return True
