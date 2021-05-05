#!/usr/bin/python3
"""
    A module to divide a matrix


"""


def matrix_divided(matrix, div):
    """
        A function to divide a matrix
    """

    if isinstance(matrix, list) is False or\
       all(isinstance(x, list) for x in matrix) is False:
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    for row in matrix:
        for number in row:
            if all(isinstance(number, (int, float))
               for number in row) is False:
                raise TypeError("matrix must be a matrix (list of lists)\
                                of integers/floats")

    for row2 in matrix:
        if len(row2) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    list_all = []

    for i in range(len(matrix)):
        list_row = []
        for j in range(len(matrix[i])):
            list_row.append(round(matrix[i][j] / div, 2))
        list_all.append(list_row)
    return list_all
