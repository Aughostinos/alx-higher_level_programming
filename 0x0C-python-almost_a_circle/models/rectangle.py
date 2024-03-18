#!/usr/bin/python3
""" module documentation """

from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self. __y = y

    def area(self):
        """public method that returns the area
           value of the Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__height):
            disp = ''
            for j in range(self.__width):
                disp += '#'
            print(disp)

    def __str__(self):
        return ('[Rectangle] ({}) {}/{} - {}/{}'
                .format(self.id,
                        self.__x,
                        self.__y,
                        self.__width,
                        self.__height))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
