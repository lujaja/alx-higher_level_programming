#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent Rectangle"""
    def __init__(self, size):
        """Initialize Square.

        Args:
            size (int): size of square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
