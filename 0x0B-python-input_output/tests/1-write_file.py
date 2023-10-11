#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file.
    if file exits overwrites and if it doesnt exist it creates

    Args:
        filename (txt): file to write to.
        text (txt): text to write in filename
    """
    with open(filename, 'w', encoding='utf-8') as fp:
        return fp.write(text)
