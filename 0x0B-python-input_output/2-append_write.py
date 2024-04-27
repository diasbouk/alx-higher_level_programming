#!/usr/bin/python3

""" For import and stuff """


def append_write(filename="", text=""):
    """ Apeends text to filename """
    with open(filename, "a+", encoding="utf-8") as file:
        return file.write(text)
