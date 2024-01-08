#!/usr/bin/python3

"""Module for sum function"""


def add_integer(a, b=98):
    """Methode to count the sum of two numbers
    could be integers or floats

    Args:
        a: first number
        b: second number

        Raises:
        TypeError: if args arent numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
