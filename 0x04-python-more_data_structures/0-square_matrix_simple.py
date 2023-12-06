#!/usr/bin/python3
import copy
def square_matrix_simple(matrix=[]):
    new_matrix = copy.deepcopy(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] * matrix[i][j]
    return new_matrix
