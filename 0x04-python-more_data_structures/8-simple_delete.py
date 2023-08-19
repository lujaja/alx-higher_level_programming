#!/usr/bin/python3
# Lujaja Luvuga

def simple_delete(a_dictionary, key=""):
    """deletes key in a dictionary"""
    if key in a_dictionary:
        del a_dictionary[key]

    return (a_dictionary)
