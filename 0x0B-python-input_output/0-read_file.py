#!/usr/bin/python3
"""
Reads from a file and prints
to stdout"""

def read_file(filename=""):
    with open(filename, "r", encoding='utf-8') as file:
        for line in file:
            print("{}".format(line), end="")
