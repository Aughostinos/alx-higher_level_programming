#!/usr/bin/python3
""" this module defines a rectangle"""


class Rectangle:
    """ empty class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """class constractor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ This is width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """this is the width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This is height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """this is the height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
