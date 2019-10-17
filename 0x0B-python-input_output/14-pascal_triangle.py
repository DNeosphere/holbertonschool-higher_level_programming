#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]
    n_list = []

    for row in range(1, n):
        n_list = [1]
        for line in range(1, row):
            elem = pascal[row - 1][line - 1] + pascal[row - 1][line]
            n_list.append(elem)
        n_list.append(1)
        pascal.append(n_list)
    return pascal
