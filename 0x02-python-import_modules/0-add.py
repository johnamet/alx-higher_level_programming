#!/usr/bin/python3
# Define the values of a and b
a = 1
b = 2

# Import the add function from add_0.py
from add_0 import add

# Calculate the result
result = add(a, b)

# Print the result using string formatting
print("{} + {} = {}".format(a, b, result))

# This code will only run if the script is executed directly
if __name__ == "__main__":
    # Any additional code you want to run when the script is executed directly
    print("{} + {} = {}".format(a, b, result))

