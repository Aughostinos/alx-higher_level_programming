#!/usr/bin/python3
""" module documentation """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute, in order."""
        if len(args) > 0:
            attr_order = ['id',
                          'size',
                          'x',
                          'y']

        for i, arg in enumerate(args):
            if i < len(attr_order):
                setattr(self, attr_order[i], arg)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

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
