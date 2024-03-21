#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(matrix[map(lambda num: num ** 2, matrix)])
