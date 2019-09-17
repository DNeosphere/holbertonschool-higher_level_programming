#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i_in = 0
    i_out = 0
    for i_out in range(len(matrix)):
        for i_in in range(len(matrix[i_out])):
            if i_in < len(matrix)-1:
                print("{:d}".format(matrix[i_out][i_in]), end=' ')
            elif i_in == len(matrix)-1:
                print("{:d}".format(matrix[i_out][i_in]))
