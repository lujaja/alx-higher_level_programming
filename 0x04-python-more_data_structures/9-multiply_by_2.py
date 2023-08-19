#!/usr/bin/python3
# lujaja Luvuga

def multiply_by_2(a_dictionary):
    """return  a dictionary with all values multiplied by 2"""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
