#!/usr/bin/python3
# Lujaja Luvuga

def print_sorted_dictionary(a_dictionary):
    """print a dictionary by ordered keys"""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
