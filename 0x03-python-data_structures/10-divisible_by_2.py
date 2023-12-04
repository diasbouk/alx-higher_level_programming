#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) <= 0:
        return None
    new_list = []
    for i in range(0, len(my_list) - 1):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
