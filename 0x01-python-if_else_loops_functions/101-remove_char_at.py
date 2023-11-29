#!/usr/bin/python3
new_str = ""
def remove_char_at(str, n):
    for i in range(0, len(str)):
        if (i != n):
            new_str[i] = str[i]
    return new_str
