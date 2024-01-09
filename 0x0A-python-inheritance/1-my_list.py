#!/usr/bin/python3
"""This is module  documentation"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """
        Public instance method
        """

        print(sorted(self))
