#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for ele in range(1, x):
            print("{}".format(my_list[ele - 1]), end="")
    except IndexError:
        print("Out of range")
