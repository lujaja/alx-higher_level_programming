#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if ((not isinstance(value, tuple)) or (len(value) != 2) or
                (num < 0 for num in value) or
                (num is not int for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
            return
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        [print("") for n in range(self.__position[1])]
        for n in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
        return

    def __str__(self):
        if self.__size == 0:
            [print("") for n in range(self.__position[1])]
            # print("")
        for n in range(self.__size):
            [print(" ", end='') for j in range(self.__position[0])]
            [print("#", end='') for k in range(self.__size)]
            if n != self.__size - 1:
                print("")
        return ("")
