#!/usr/bin/python3
import math

def square_matrix_map(matrix=[]):
    return matrix[map(lambda num: math.sqrt(num), matrix)]
