#!/usr/bin/python3
# Lujaja Luvuga

def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position"""
    if isinstance(my_list, list):
        if (idx < 0) or (idx > (len(my_list) - 1)):
            return (my_list)
        else:
            new_list = my_list.copy()
            new_list[idx] = element
    return (new_list)
