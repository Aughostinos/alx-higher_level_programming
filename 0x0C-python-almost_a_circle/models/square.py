#!/usr/bin/python3
""" module documentation """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Return the string representation of the Square."""
        return ('[Square] ({}) {}/{} - {}'
                .format(self.id,
                        self.x,
                        self.y,
                        self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
