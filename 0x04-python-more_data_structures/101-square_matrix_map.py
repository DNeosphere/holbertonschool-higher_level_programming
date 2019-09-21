#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda out: list(map(lambda in_l: in_l ** 2, out)), matrix))
