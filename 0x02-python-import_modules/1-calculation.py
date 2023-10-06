#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
print("{a} + {b} = {add}\n{a} - {b} = {sub}"
      .format(a=a, b=b, add=add(a, b), sub=sub(a, b)))
print("{a} * {b} = {mul}\n{a} / {b} = {div}"
      .format(a=a, b=b, mul=mul(a, b), div=div(a, b)))
