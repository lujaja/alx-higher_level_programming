#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of text file.

    Args:
        filename (txt): file to append to
        text (txt): text to append to file
    Return:
        number of characters appended
    """
    with open(filename, "a", encoding='utf-8') as fp:
        return fp.write(text)
