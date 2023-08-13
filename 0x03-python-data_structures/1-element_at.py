#!/usr/bin/python3
# 1-element_at.py
# Lujaja Luvuga

def element_at(my_list, idx):
    """Dunction that retrieves an element from a list like in C"""
    if (idx < 0) or (idx > (len(my_list) - 1)):
        return None
    else:
        return (my_list[idx])
