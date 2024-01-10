#!/usr/bin/python3
"""python input output module"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    and returns the number of characters"""

    with open(filename, 'w') as file:
        return file.write(text)

