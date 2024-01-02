#!/usr/bin/python3
"""
This is a module that defines the square class
"""


class Square:

    """
    This is a class that defines a square with its size.

    Attributes:
    __size: size of the square.
    """
    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            rise TypeError("size must be an integer")
        if value < 0:
            rise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        public instance method that return the area of the square
        """
        return self.__size ** 2
