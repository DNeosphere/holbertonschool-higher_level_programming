#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    else:
        i_in = 0
        i_out = 0
        for i_out in range(len(matrix)):
            for i_in in range(len(matrix[i_out])):
                if i_in is not len(matrix)-1:
                    print("{:d} ".format(matrix[i_out][i_in]), end='')
                else:
                    print("{:d}".format(matrix[i_out][i_in]), end='')
            print()
