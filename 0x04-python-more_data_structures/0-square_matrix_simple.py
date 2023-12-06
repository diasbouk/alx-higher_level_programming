#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = 0
    j = 0
    new_matrix = [[]]
    for i in  range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] * matrix[i][j]
    return new_matrix
