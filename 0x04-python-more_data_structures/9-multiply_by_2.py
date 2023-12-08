#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for elem in a_dictionary:
        number = map(lambda num: num * 2, elem)
        new_dict.append(list(number))
    return new_dict
