#!/usr/bin/python3
# print alphabet

""" print alphabet in lowercase not followed by a new line. """
for letter in range(97, 123):
    if (chr(letter) == 'e') or (chr(letter) == 'q'):
        continue
    print("{}".format(chr(letter)), end="")
