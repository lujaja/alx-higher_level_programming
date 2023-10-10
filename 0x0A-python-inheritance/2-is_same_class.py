#!/usr/bin/python3
# Lujaja Luvuga
"""Function Definition"""


def is_same_class(obj, a_class):
    """checks if an objects is an instance of specified class.

    Args:
        obj (object): object to check
        a_class (class): class to check in
    """
    if type(obj) is a_class:
        return True
    return False
