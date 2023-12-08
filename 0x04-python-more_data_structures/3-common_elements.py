#!/usr/bin/pytohn3
def common_elements(set_1, set_2):
    sorted_list = []
    for el in set_1:
        if el in set_2:
            sorted_list.append(el)
    return sorted_list
