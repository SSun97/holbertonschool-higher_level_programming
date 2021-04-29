#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        list1 = []
        for item in matrix:
            list1.append(list(map(lambda x: x**2, item)))
        return list1
    else:
        return []
