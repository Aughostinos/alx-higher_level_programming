#!/usr/bin/python3
"""
This module define a square class
"""


class Square:

    """
    This is a class that defines a square with its size.

    Attributes:
    __size: size of the square.
    """
    def __init__(self, size=0):
        """
        create a new square

        Args:
            size: the size of the square
        """
        self._size = size

    @property
    def size(self):
        """
        property method to get the size
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        property method to set the size
        """
        if not isinstance(value, int):
            rise TypeError("size must be an integer")
        if value < 0:
            rise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        public instance method that return the area of the square
        """
        return self._size ** 2
