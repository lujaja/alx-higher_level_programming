#!/usr/bin/python3
# Lujaja Luvuga
"""Define class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent Rectangle"""
    def __init__(self, width, height):
        """Initialize Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate area of the Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """prints informal representation of Rectangle"""
        string = "[{:s}] ".format(str(self.__class__.__name__))
        string += str(self.__width) + "/" + str(self.__height)
        return string
