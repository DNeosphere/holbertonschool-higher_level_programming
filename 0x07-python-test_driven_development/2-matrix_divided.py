#!/usr/bin/python3
"""
Divides a matrix or lists if the elements are integers
>>> matrix_divided(matrix, divisor)
Outuput, every item with 2 float points
"""


def matrix_divided(matrix, div):
    """
    Function that divdes a matrix of integers
    """
    m_error = 'matrix must be a matrix (list of lists) of integers/floats'

    if matrix == []:
        raise TypeError(m_error)

    if matrix is None:
        raise TypeError(m_error)

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(matrix, list) and isinstance(matrix, list):
        raise TypeError(m_error)

    if not isinstance(matrix[0], list):
        raise TypeError(m_error)

    comp_l = len(matrix[0])
    n_matrix = []

    for row in range(len(matrix)):

        if not isinstance(matrix[row], list):
            raise TypeError(m_error)

        elif len(matrix[row]) != comp_l:
            raise TypeError('Each row of the matrix must have the same size')

        n_matrix.append([])

        for elem in range(len(matrix[row])):

            if (type(matrix[row][elem]) is not int and
                    type(matrix[row][elem]) is not float):
                raise TypeError(m_error)

            res = round(matrix[row][elem] / div, 2)
            n_matrix[row].append(res)

    return n_matrix
