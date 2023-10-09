#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for vector in matrix:
        for j in vector:
            print("{}".format(j), end=" ")
        print()
