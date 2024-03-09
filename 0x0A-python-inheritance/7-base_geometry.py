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
            raise TypeError("<{} must be an integer".format(name))
        if not value > 0:
            raise ValueError("{} must be greater than 0".format(name))
