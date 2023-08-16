#!/usr/bin/python3
# Lujaja Luvuga

def only_diff_elements(set_1, set_2):
    """return a set of all elements present in only one set"""
    return (list(set_1 ^ set_2))
