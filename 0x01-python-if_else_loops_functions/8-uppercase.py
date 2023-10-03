#!/usr/bin/python3
def uppercase(str):
    str = "{}".format(''.join(chr(ord(i))
                              if ord(i) < 97 else chr(ord(i) - 32)
                              for i in str))
    print(str)
    return str
