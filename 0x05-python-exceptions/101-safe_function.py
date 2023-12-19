#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as err:
        print("Excepiton: {}".format(err), file=stderr)
    except IndexError as err:
        print("Exception: {}".format(err), file=stderr)
