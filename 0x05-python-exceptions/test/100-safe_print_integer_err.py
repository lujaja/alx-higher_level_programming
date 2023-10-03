#!/usr/bin/python3
# Lujaja luvuga <jarzcyber@gmail.com>

import sys


def safe_print_integer_err(value):
    """ prints an integer

    Args:
        value (int): function argument

    Return:
        True if value has been correctly printed else false
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
