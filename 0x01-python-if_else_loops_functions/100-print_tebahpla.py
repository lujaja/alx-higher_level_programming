#!/usr/bin/python3
# Lujaja

"""Prints the ASCII alphabet, in reverse order"""
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end='')
    if i == 0:
        i = 32
    else:
        i = 0
