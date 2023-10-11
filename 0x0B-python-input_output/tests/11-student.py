#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class Student"""


class Student:
    """Represent student."""
    def __init__(self, first_name, last_name, age):
        """Initiliazer.

        Args:
            first_name (str): parameter 1
            last_name (str): parameter 2
            age (int) parameter 3
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dict representation of a Student"""
        if (type(attrs) is list) and all(type(ele) is str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance

        Args:
            json (obj): parameter
        """
        for k, v in json.items():
            setattr(self, k, v)
