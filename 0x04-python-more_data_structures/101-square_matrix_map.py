#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda out: list(map(lambda in_: in_ ** 2, out)), matrix))
