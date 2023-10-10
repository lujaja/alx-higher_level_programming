#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class BaseGeometry"""
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
