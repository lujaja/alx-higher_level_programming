#!/usr/bin/python3
# 2-replace_in_list.py

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list , in reversed order"""
    if isinstance(my_list, list):
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))
