#!/usr/bin/python3
"""This is the module"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object
    is an instance of, or if the object is an
    instance of a class that inherited from,
    the specified class ; otherwise False."""

    if type(obj) is a_class:
        return True
    else:
        return False
