#!/usr/bin/python3
def weight_average(my_list=[]):
    scores = 0
    sums = 0
    if len(my_list) > 0:
        dict(my_list)
        for elem in my_list:
            sums += elem[1]
            scores += elem[0] * elem[1]
        return scores / sums
    return 0
