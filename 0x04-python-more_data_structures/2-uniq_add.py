#!/usr/bin/python3
# Lujaja Luvuga

def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    sam = 0
    for num in list(set(my_list)):
        sam += num

    return (sam)
