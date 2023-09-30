#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class square"""


class Square:
    """Represent square."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def __eq__(self, lujaja):
        return (self.area() == lujaja.area())

    def __ne__(self, lujaja):
        return (self.area() != lujaja.area())

    def __gt__(self, lujaja):
        return (self.area() > lujaja.area())

    def __ge__(self, lujaja):
        return (self.area() >= lujaja.area())

    def __lt__(self, lujaja):
        return (self.area() < lujaja.area())

    def __le__(self, lujaja):
        return (self.area() <= lujaja.area())
