#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    for i in range(77, 103):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** (b / i))
        except Exception:
            result = b + a
            break

    return result
