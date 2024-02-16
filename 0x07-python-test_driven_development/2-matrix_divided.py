#!/usr/bin/python3
"""
Function to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix (list of lists): The matrix
        div (int/float): The divisor

    Returns:
        list of lists: New matrix with elements divided by div
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(element / div, 2) for element in row] for row in matrix]
