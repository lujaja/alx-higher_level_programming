#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Class Student Definition"""


class Student:
    """Represent a student."""
    def __init__(self, first_name, last_name, age):
        """Initializer.

        Args:
            first_name (str): student first name.
            last_name (str): student last name.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictonary representation of student"""
        return self.__dict__
