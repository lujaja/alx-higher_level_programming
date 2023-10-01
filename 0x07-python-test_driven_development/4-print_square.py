#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define a function to print a square"""


def print_square(size):
    if (not isinstance(size, int)) or (isinstance(size, float) and size < 0) :
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        [print("#", end="") for j in range(int(size))]
        print("")
