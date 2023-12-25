#!/usr/bin/python3
import sys


def main(*args):
    result = 0

    for i in args:
        result += int(i)
    print(result)


if __name__ == "__main__":

    args = sys.argv[1:]
    main(*args)
