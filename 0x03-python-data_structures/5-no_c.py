#!/usr/bin/python3
# 5-no_c.py
# Lujaja Luvuga

def no_c(my_string):
    """removes all characters c and C from string"""
    if isinstance(my_string, str):
        str_copy = "".join(c for c in my_string if c != 'c' and c != 'C')
        return (str_copy)
