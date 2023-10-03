#!/usr/bin/python3
# 1-safe_print_integer.py
# Lujaja Luvuga <jarzcyber@gmail.com>

def safe_print_integer(value):
    """ Prints an Integer

    Args:
        value: can be any type (integer, string, etc).

    Return:
        True if value correctly printed, else false.
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
