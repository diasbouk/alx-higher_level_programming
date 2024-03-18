#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        idx = len(element) - 1
        for number in element:
            print("{:d}".format(number), end="")
            if number != element[idx]:
                print(" ", end="")
        print("")
