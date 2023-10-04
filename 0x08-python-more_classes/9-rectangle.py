#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define a rectangle"""


class Rectangle:
    """Represent a Rectangle.

    Attributes:
        number_of_instances (int): count number of instances instatiated
        print_symbol (any): class attribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.__width = width
        self.__height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """Get current rectangle width.
        Return:
            width (int):
        """
        return (self.__width)

    @property
    def height(self):
        """Get current rectangle height.
        Return:
            width (int):
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """set new rectangl width

        Args:
            value (int): new rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, value):
        """Set new rectangle height.

        Args:
            value (int): new rectangle height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate Rectangle Area.

        Return:
            area (int)
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate Rectangle perimeter.

        Return:
            perimeter (int)
        """
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare rectangle based on area.

        Args:
            rect_1 (Rectangle): parameter 1
            rect_2 (Rectangle): parameter 2
        Return:
            biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance if Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return new rectangle instance

        Args:
            size (int): new rectangle size
        Return size, size
        """
        return (cls(size, size))

    def __str__(self):
        """print informal representation of a rectangle relevant
        to the user"""
        if (self.__width == 0) or (self.__height == 0):
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i < (self.__height - 1):
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Print formal representation of a Rectangle relevant to developers
        and can be used to recreate the object using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Detects instance deletion and print a message"""
        self.number_of_instances -= 1
        print("Bye rectangle...")
