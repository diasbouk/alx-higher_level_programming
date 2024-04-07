#!/usr/bin/python3 

def add_integer(a, b=98):
    if type(a) != int or type(a) != float:
        raise TypeError("a must be an interger")
    if type(b) != int or type(b) != float:
        raise TypeError("b must be an interger")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
