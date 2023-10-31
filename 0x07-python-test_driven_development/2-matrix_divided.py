#!/usr/bin/python3
"""The module divides all element in a matrix by a number"""


def matrix_divided(matrix, div):
    """The module divides each element in a matrix
        by a div

    Args:
        matrix (list): A list of lists making up a matrix
        div (int/float): An integer or float that divides the elements

    Returns:
        A new matrix with each element divided by the div rounded to
            2 decimal places
    The function only accepts a matrix of integers or float (list of lists)

    >>> matrix = [[2, 2, 4], [1, 2, 2]]
    >>> matrix_divided(matrix, 2) #doctest: +NORMALIZE_WHITESPACE
        [[1.0, 1.0, 2.0], [0.5, 1.0, 1.0]]

    >>> matrix = ["b", 1, 2]
    >>> matrix_divided(matrix, 5) #doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
        TypeError: matrix must be a matrix (list of lists) of integers/floats
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_l = [len(row) for row in matrix]

    if len(set(row_l)) != 1:
        raise Exception("Each row of the matrix must have the same size")
    try:
        new_matrix = [[round(element/div, 2) for element in row] for row in matrix]
    except Exception as e:
        print(e)

    return new_matrix
