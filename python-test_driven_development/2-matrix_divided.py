#!/usr/bin/python3
"""This module will divide the elements of a matrix by a given divisor,
 appending the quotient to a new matrix"""


def matrix_divided(matrix, div):
    """Divide elements of matrix by div.

    Matrix elements and divisors must be integers or floats.

    Parameters:
        matrix: matrix to divide
        div: divisor
    """
    if type(div) is not float and type(div) is not int:  # check div type
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    x = len(matrix)  # take number of rows
    ref_row = 0
    if x is not 0 and type(matrix[x - 1]) is list and len(matrix[x - 1]) > 0:
        ref_row = len(matrix[x - 1])  # use last row as reference
    n_matrix = [[] for row in range(x)]  # Create new matrix with empty rows

    for row in range(x):
        if len(matrix[row]) != ref_row:
            raise TypeError('Each row of the matrix must have the same size')
        for item in matrix[row]:
            if type(item) is not float and type(item) is not int:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            n_matrix[row].append(round(item / div, 2))  # Append the quotient rounded to 2 decimal places

    return n_matrix
