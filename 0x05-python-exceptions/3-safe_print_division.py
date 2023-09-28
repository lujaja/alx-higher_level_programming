#!/usr/bin/python3
# 3-safe_print_division.py
# Lujaja Luvuga <jarzcyber@gmail.com>

def safe_print_division(a, b):
    """ Divides two integrs and prints the result

    Args:
        a: parameter
        b: parameter

    Return:
        The value of the division, otherwise None.
    """

    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
