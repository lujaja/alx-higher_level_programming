#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define a Rectangle"""


class Rectangle:
    """Represent a rectangle

    Attributes:
        number_of_instances (int): The  umber of rectangle instances
        print_symbol (any): Symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle.

        Args:
            width (integer): parameter 1.
            height (integer): parameter 2.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get current width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set new width.
        Args:
            value (int): parameter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get current height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set new height.
        Args:
            value (integer): parameter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of rectngle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return informal representations relevant to the user
        about an object"""
        rect = []
        if (self.__width == 0) or (self.__height == 0):
            return ""
        for i in range(0, self.__height):
            [rect.append(str(self.print_symbol)) for j in
                range(0, self.__width)]
            if i != (self.height - 1):
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return forma representation relevant to recreate the object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Detects deltion of an instance and prints a message"""
        self.number_of_instances -= 1
        print("Bye rectangle...")
