#!/usr/bin/python3

i = 97
while i <= 122:
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
    i = i + 1
