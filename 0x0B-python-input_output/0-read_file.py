#!/usr/bin/python3
"""python input output module"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, 'r') as file:
        print(file.read(), end='')
