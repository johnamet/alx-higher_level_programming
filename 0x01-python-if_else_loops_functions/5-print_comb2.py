#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("{}".format('0' + str(i)), end=", ")
    elif i == 99:
        print("{}".format(str(i) + '\n'), end="")
    else:
        print("{}".format(str(i)), end=", ")
