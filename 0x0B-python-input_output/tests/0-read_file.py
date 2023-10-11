#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Function Definition"""


def read_file(filename=""):
    """Reads a text file in UTF8 and prints it to stdout

    Args:
        filename (txt): text file to read
    """
    with open(filename, encoding="utf-8") as fp:
        print("{}".format(fp.read()), end='')
