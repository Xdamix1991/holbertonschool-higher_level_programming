#!/usr/bin/python3
from calculator_1 import mul, div, sub, add
a = 10
b = 5
addition = add(a, b)
print("{} + {} = {}".format(a, b, addition))
substraction = sub(a, b)
print("{} + {} = {}".format(a, b, substraction))
multiplication = mul(a, b)
print("{} + {} = {}".format(a, b, multiplication))
division = div(a, b)
print("{} + {} = {}".format(a, b, division))
if __name__ == "__main__":
    pass
