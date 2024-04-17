#!/usr/bin/python3

""""
For modules and other stuff
"""


def read_file(filename=""):
    """ Reads from a file and prints to stdout """
    with open(filename, "r+", encoding="utf-8") as f:
        print(line for line in f)
