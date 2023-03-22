#!/usr/bin/python3
""" Module for Pascal's Triangle """


def pascal_triangle(n):
    pascal = [[1]]

    if n <= 0:
        return []

    if n == 1:
        return pascal

    for i in range(1, n):
        l = -1
        r = 0
        tri_row = []
        for j in range(i + 1):
            num = 0
            if l > -1:
                num += pascal[i - 1][l]
            if r < i:
                num += pascal[i - 1][r]
            l += 1
            r += 1
            tri_row.append(num)
        pascal.append(tri_row)
    return pascal
