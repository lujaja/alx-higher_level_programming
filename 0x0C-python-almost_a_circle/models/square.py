#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent class Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer.

        Attributes:
            size (int): size of square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return informal representation of the square"""
        string = ("[{:s}] ({:d}) {:d}/{:d} - {:d}".format
                  (self.__class__.__name__, self.id, self.x, self.y,
                   self.width))
        return str(string)

    @property
    def size(self):
        """Get current size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set new size of square"""
        self.witdh = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes.

        Args:
            args (int): non-keyworded arguments
            kwargs (str, int): keyworded arguments
        """
        if args and len(args) > 0:
            ele = 0
            for arg in args:
                if ele == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = arg
                elif ele == 1:
                    self.width = arg
                elif ele == 2:
                    self.x = arg
                elif ele == 3:
                    self.y = arg
                ele += 1
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
        }
