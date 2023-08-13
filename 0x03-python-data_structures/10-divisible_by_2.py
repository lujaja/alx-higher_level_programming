#!/usr/bin/python3
# Lujaja Luvuga

def divisible_by_2(my_list=[]):
    """find all multiple of 2 in a list"""
    if isinstance(my_list, list):
        lst = []
        for i in range(len(my_list)):
            lst.append(bool(my_list[i] % 2 == 0))

        return (lst)
