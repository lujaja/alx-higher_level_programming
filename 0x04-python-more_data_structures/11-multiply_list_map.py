#!/usr/bin/python3
# Lujaja Luvuga

def multiply_list_map(my_list=[], number=0):
    """function that returns a list with all values multiplied by a number
    without using any loops
    """
    new_list = my_list.copy()
    return (list(map(lambda x: x * number, new_list)))
