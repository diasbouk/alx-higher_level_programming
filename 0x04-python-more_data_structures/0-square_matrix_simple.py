#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        sub_list = []
        for element in row:
            sub_list.append(element ** 2)
        new_matrix.append(sub_list)
    return new_matrix
