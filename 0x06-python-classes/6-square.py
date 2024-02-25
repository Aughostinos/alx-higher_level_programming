#!/usr/bin/env python3
"""
This is a module that defines the square class
"""


class Square:
    """
    This is a class that defines a square with its size.

    Attributes:
    _size: size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
        size: private attribute
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple),
        or len(value) != 2,
        or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be  a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        public instance method that returns the area of the square
        """
        return self._size ** 2

    def my_print(self):
        """
        public instance method that prints the square
        """
        if self._size == 0:
            print("")
            return

        print("\n" * self._position[1], end="")

        for i in range(self._size):
            print(" " * self._position[0], end="")
            print('#' * self._size)
