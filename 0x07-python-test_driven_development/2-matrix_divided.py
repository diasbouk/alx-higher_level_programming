#!/usr/bin/python3

def matrix_devided(matrix, div):
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if [type(n) for n in matrix] is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
