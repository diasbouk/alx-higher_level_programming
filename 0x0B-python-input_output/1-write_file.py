#!/usr/bin/python3

""" Docs """

def write_file(filename="", text=""):
    """ writes to file """
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(text)
