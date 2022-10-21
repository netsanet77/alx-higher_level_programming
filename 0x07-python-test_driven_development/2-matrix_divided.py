#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        martix (list): a list of lists of integers or floats
        div (intger/float): number
    Return: new matrix
    """
    new_matrix = [[]]
    if type(matrix) != list and not isinstance([ele for ele in matrix], int):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        new_matrix = list(map(lambda a: round(a / div, 2), i))
    return new_matrix
