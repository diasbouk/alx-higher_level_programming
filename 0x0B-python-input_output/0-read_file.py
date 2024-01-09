#!/usr/bin/python3
"""
Reads from a file and prints
to stdout"""

def read_file(filename=""):
    with open(filename, "r", encoding='UTF-8') as file:
        print("{}".format(file.read()), end='')
