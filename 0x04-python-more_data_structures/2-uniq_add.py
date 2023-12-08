#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new_list = []
    for element in my_list:
        if element not in new_list:
            result += element
            new_list.append(element)
    return result
