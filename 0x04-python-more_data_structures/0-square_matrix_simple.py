#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    n_matrix = matrix[:]
    for i in range(len(n_matrix)):
        n_matrix[i] = list(map(lambda x: x**2, n_matrix[i]))
    return n_matrix
