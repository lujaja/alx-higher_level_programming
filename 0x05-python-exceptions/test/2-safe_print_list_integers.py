#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Lujaja Luvuga <jarzcyber@gmail.com>

def safe_print_list_integers(my_list=[], x=0):
    """ Print the first x elements of a list that are integers

    Args:
        my_list (list): list to print from.
        x (int): the number of elements of my_list to print.

    Return:
        Number of integers printed.
    """

    ret = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
