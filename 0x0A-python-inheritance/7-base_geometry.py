#!/usr/bin/python3
# Lujaja Luvuga
"""Define class BaseGeometry"""


class BaseGeometry:
    """Represent BaseGeometry"""
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name (str): parameter 1
            value (int): parameter to validate
        """
        if type(value) is not int:
            raise TypeError("{:s} must ne an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
