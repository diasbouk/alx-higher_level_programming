#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        str =""
        for i in range(0, x):
            str += str(my_list[i])
        return str
    except IndexError:
        retrun ""
