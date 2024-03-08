#!/usr/bin/python3
"""This is geometry module"""


class BaseGeometry:
    """
    This is Geometry class
    """

    def area(self):
        """
        Public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if not value > 0:
            raise ValueError("<name> must be greater than 0")
