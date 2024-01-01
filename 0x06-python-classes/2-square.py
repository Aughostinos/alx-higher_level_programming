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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
