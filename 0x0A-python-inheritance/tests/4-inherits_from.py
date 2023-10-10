#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Function Definition"""


def inherits_from(obj, a_class):
    """checks is an objects is an instance of a class that inherited
    directly or indirectly from the specified class

    Args:
        obj (any): object to check
        a_class (class): class to check from
    Return:
        True: if the object is an instance of a class that inherited
        (directly or indirectly) from specified class
        False: otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
