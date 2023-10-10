#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Function Definition"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of, or if the object is
    an instance of a class that inherits from the specified class.

    Args:
        obj (any): object to check.
        a_class (class) class to check in
    Return:
        True: if its True.
        False: otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
