#!/usr/bin/python3

def safe_print_division(a, b):

    result = None
    try:
        result = a / b
    except (TypeError, ZeroDivisionError, NameError):
        return result
    finally:
        try:
            print("Inside result: {:.1f}".format(result))
        except TypeError:
            print("Inside result: {}".format(result))

    return result
