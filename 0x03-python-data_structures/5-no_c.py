#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            new_str += idx
    return new_str
