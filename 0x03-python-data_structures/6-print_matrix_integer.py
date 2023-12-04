#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for number in element:
            print("{:d} ".format(number),end="")
        print("")
