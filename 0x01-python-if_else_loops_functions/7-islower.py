#!/usr/bin/python3
def islower(c):
    for i in range(97, 122):
        if chr(i) == c:
            return True
    return False
