#!/usr/bin/python3
'''this is Python - Test-driven development module'''


def add_integer(a, b=98):
    '''function that adds 2 integers

    Args:
        a: first number to add of type int or float
        b: second number, of type int of float

    Returns:
        int: a + b
    '''

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    elif a == float('inf') or b == float('inf'):
        raise ValueError("a must be an integer")

    else:
        a = int(a)
        b = int(b)

        return (a + b)
