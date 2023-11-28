#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str) + 1):
        if ord(str[i]) >= 97 and i <= 122:
            print("{}".format(chr(ord(str[i]) + 32)))
        else:
            print("{}".format(str[i]))
