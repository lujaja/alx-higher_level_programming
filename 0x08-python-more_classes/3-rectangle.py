#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define A rectangle"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
        width (integer): first parameter.
        height (integer): second parameter.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get cuurent width"""
        return self.__width

    @property
    def height(self):
        """Get current Height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Set new width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set new height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes area of a rectangle
        Method used:
            area = width multiplied by height
        Return:
            area of a rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes perimeter of a rectangle.
        method used:
            perimeter = ((height _ width) * 2)
        Return:
            perimeter
        """
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        for i in range(0, self.__height):
            [print("#", end="") for j in range(0, self.__width)]
            print("")
        return ("")
