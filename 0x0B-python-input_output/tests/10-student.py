#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class Student"""


class Student:
    """Represent student"""
    def __init__(self, first_name, last_name, age):
        """Initializer.

        Args:
            first_name (str): parameter 1
            last_name (str): parameter 2
            age (int):  parameter 3
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary

        Args:
            attrs (obj): parameter
        """
        if (type(attrs) is list) and all(type(ele) is str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
