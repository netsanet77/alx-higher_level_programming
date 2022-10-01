#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = matrix.copy()
    length = len(squared_matrix)
    for i in range(length):
        squared_matrix[i] = list(map(lambda a: a ** 2, squared_matrix[i]))
    return squared_matrix
