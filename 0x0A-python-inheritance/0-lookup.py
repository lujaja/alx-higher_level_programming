#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Function definition"""


def lookup(obj):
    """checks available attributes and methods of an object.

    Args:
        obj (object): parameter
    Return:
        list of available attributes and methods of an object.
    """
    if not isinstance(obj, object):
        return []
    return list(dir(obj))
