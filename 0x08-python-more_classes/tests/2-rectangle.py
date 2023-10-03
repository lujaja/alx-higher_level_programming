#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define a rectangle"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle.
        Args:
            width (integer): width of the Rectangle.
            height (integer): height of the Rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get current rectangle width.
        Return:
            current rectangle width.
        """
        return self.__width

    @property
    def height(self):
        """Get current rectangle height.
        Return:
            current height.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Set new rectangle width.
        Args:
            value (integer): new width must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set new height.
        Args:
            value (integer): must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and return the area of the rectangle.

        area method used:
            area of a rectangle = width multiplied by height.
        Return:
            Area of a rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes and return the perimeter of a rectangle.

        perimeter method used:
            perimeter of a rectangle = 2(width + height)
        Return:
            Perimeter
        """
        return ((self.__width + self.__height) * 2)
