#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class square"""


class Square:
    """Represent square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize the sqaure.

        Args:
            size (int): size of the new square.
            position (int , int): position coodinates of the new square.
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get current size of square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Set new size of current square.

        Args:
            value (int): New size og the square.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must >= 0")
        self.__size = value

    @property
    def position(self):
        """Get current position coodinates of the square."""

        return (self.__position)

    @position.setter
    def position(self, value):
        """Set new position coodinates of the square.

        Args:
            value (int, int): new square coodinates.
        """

        if (not isinstance(value, tuple) or (len(value) != 2) or\
                (not isinstance(num, int) for num in value) or\
                (num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
            return

        self.__postion = value

    def area(self):
        """Current square area"""

        return (self.__size ** 2)

    def my_print(self):
        """prints square with character # to stdout."""

        if self.__size == 0:
            print("")
            return
        [print("") for n in range(0, self.__position[1])]
        for n in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if n != (self.__size - 1):
                print("")
