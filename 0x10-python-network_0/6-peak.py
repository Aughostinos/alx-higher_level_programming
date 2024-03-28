#!/usr/bin/python3
"""find a peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of integers"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    else:
        return max(list_of_integers)
