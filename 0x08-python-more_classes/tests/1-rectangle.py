#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define a rectangle"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width (integer): width of the rectangle.
            height (integer): height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get current rectangle width.
        Return:
            current rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set new rectangle width.

        Args:
            value (integer): new rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get current rectangle height.
        Return:
            current rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set new height for the rectangle

        Args:
            value (integer): New rectangle height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
