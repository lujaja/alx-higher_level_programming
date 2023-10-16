#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Deine class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represent Rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer.

        Attributes:
            width (int): rectangle width
            height (int): rectangke height
            x (int): x coordinate of rectangle
            y (int): y coordinate of rectangle
            id (int): unique identifier of rectangle
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 1:
            raise ValueError('width must be > 0')
        elif type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 1:
            raise ValueError('height must be > 0')
        elif type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        elif type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
            super().__init__(id)

    @property
    def width(self):
        """Get Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set new rectangle width.
        Attributes:
            value (int): new rectangle width.
        raise:
            TypeError: if value is not an integer
            ValueErroe: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Get Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set Rectangle height.

        Attributes:
            value (int): new rectangle height
            raise: TypeError: if value is not an integer
            ValueErroe: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Get x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set new x coordinate value.

        Attribute:
            value (int): new x coordinate value
        raise:
            TyperError: if x is not an integer
            ValueError: if x is less than 0
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Get y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set new y coordinate.

        Attributes:
            value (int): new y coordinate value
            raise:
                TyperError: if y is not an integer
                ValueError: if y is less than 0
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle instance.

        Return:
            area
        """
        return self.__width * self.__height

    def display(self):
        """Print in stdout the rectangle instance with the character #"""
        if (self.__width == 0) or (self.__height == 0):
            print("")
            return
        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end='') for x in range(self.__x)]
            [print("#", end='') for w in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.
        Attributes:
            args (int)
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
                This is a "no-keyword argument" - Argument order is super
                important
            kwargs (str, int)
                keyworded argument, it has a string key and an int value
            """
        if args is not None and len(args) > 0:
            ele = 0
            for arg in args:
                if ele == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif ele == 1:
                    self.width = arg
                elif ele == 2:
                    self.height = arg
                elif ele == 3:
                    self.x = arg
                elif ele == 4:
                    self.y = arg
                ele += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """Return informal representation of the class relevant to the user"""
        string = ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format
                  (self.__class__.__name__, self.id, self.__x, self.__y,
                   self.__width, self.__height))
        return str(string)

    def to_dictionary(self):
        """Return dictionary representation of a rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }
