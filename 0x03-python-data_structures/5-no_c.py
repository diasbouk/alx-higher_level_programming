#!/bin/usr/python3
def no_c(my_string):
    idx = 0
    new_str = ''
    for idx in range(0, len(my_string) - 1):
        if my_string[idx] != 'c' and my_string[idx] != 'C':
            new_str += my_string[idx]
        idx += 1
    return new_str
