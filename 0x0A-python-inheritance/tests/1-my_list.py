#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class Mylist that inherits rom list"""


class MyList(list):
    """Represent Mylist"""
    def __init__(self):
        """Initialize the object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list in ascending order"""
        print(sorted(self))
