#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for vector in matrix:
        v_size = len(vector)
        for j in vector:
            print("{:d}".format(j, " " if vector[-1] != j else ""), end="")
