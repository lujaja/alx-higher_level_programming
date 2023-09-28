#!/usr/bin/python3
# 0-safe_print_list.py
# lujaja Luvuga <jarzcyber@gmail.com>

def safe_print_list(my_list=[], x=0):
    """ Print x elements of a list

    Args:
        my_list (list): the list ot print elements from.
        x: number of elements to print:

    Return:
        Number of elements printed.
    """
    ret = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            ret += 1
        except (IndexError, ValueError):
            break
    print("")
    return (ret)
