#!/usr/bin/python3
import sys
def main(*args):
    
    if len(args) == 1:
        print("1 argument:")
    else:
        print("{} arguments{}".format(len(args), "." if len(args) == 0 else ":"))

    if len(args) != 0:
        for i in range(len(args)):
            print("{}: {}".format(i+1, args[i]))

if __name__ == "__main__":
    args = sys.argv[1:]
    main(*args)
