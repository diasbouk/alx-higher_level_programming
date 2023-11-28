#!/usr/bin/python3
def pow(a, b):
    if b > 0:
        for i in range(1, b):
            a *= a
        return a
    elif b < 0:
        for i in range(1, -b):
            a *= a
        return 1 / a
    else:
        return 1
