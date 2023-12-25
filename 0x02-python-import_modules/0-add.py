#!/usr/bin/python3
from add_0 import add
# Define the values of a and b
a = 1
b = 2
# Calculate the result
result = add(a, b)

# This code will only run if the script is executed directly
if __name__ == "__main__":
    # Any additional code you want to run when the script is executed directly
    print("{} + {} = {}".format(a, b, result))
