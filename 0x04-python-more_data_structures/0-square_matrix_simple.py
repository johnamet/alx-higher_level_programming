#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    m_matrix = [list(map(lambda x: x**2, i)) for i in matrix]
    return m_matrix
