#!/usr/bin/python3
"""This module multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """This function performs matrix multiplication
        Args:
            m_a (list): the matrix A
            m_b (list): the matrix B

        Returns:
            (:obj:list): the result matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    row_a_l = [len(row) for row in m_a]
    row_b_l = [len(row) for row in m_b]

    if len(set(row_a_l)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(row_b_l)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # To multiply two matrices the number of rows in matrix A
    # needs to be equal to the number of columns in matrix B
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []

    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        new_matrix.append(row)

    return new_matrix
