#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@hmail>
"""Define a rectnagle"""


class Rectangle:
    """Represent a rectangle.

    Atributes:
        number_of_instances (int): class parameter
        print_symbol (any): class parameter
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width (integer): private parameter.
            height (integer): private parameter.
        """
        self.__width = width
        self.__height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """Get current width"""
        return self.__width

    @property
    def height(self):
        """Get current height"""
        return self.__height

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

    @height.setter
    def height(self, value):
        """Set new height.

        Args:
            value (int): parameter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of a rectangle.

        Return:
           area (int)
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate perimeter of a rectangle.

        Return:
            perimeter (int)
        """
        return 2 * (self.__width + self.__perimeter)

    def __str__(self):
        """Return informal string representation relevant to the user"""
        rect = []
        if (self.__width == 0) or (self.__height == 0):
            return ""
        for i in range(0, self.__height):
            [rect.append(str(self.print_symbol)) for j in
                range(0, self.__width)]
            if i < (self.__height - 1):
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return formal string representation relevant to developers"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Detects instance deletion and print a message"""
        self.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle best on square.

        Args:
            rect_1 (object): parameter
            rect_2 (object): parameter
        Return:
            biggest triangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
