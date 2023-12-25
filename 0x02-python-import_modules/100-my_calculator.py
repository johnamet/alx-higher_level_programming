#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main(*args):
    num_args = len(args)
    args_map = {"+": add, "-": sub, "*": mul, "/": div}
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if args[1] not in list(args_map.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            operator = args_map[args[1]]
            result = operator(int(args[0]), int(args[2]))

    print("{} {} {} = {}".format(args[0], args[1], args[2], result))


if __name__ == "__main__":
    args = sys.argv[1:]
    main(*args)
