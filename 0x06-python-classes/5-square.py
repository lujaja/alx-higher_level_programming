#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class square."""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): size to the new square.
        """

        self.__size = size

    @property
    def size(self):
        """Get the cuurent size of the square."""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Set new size of square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """Prints squres with character #"""

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print("")
