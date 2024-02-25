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
    def __init__(self, size=0):

        """
        Args:
        size: private attrinute
        """
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        public instance method that return the area of the square
        """
        return self._size ** 2

    def my_print(self):
        """
        public instance method that print the square
        """
        for i in range(self._size):
            print('#'*self._size)
