#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda sub: list(map(lambda x: x*x, sub)), matrix))
