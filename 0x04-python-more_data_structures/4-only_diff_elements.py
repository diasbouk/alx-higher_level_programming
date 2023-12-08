#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = []
    for el in set_1:
        if el not in set_2:
            od_set.append(el)
    for elem in set_2:
        if elem not in set_1:
            od_set.append(elem)
        return od_set
