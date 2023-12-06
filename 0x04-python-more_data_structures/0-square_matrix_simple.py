#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for list in matrix:
        new_matrix += []
        for integer in list:
            new_matrix += integer * integer
    return new_matrix
