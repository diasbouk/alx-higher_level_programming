#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(matrix[list(map(lambda num: num ** 2, matrix))])
