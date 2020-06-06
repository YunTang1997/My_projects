# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/6
desc: 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


import numpy as np


def findNumberIn2DArray(matrix, target):
    matrix = np.mat(matrix)
    print(matrix[-1, -1])
    n, m = matrix.shape[0], matrix.shape[1]
    i, j = n-1, 0
    while i >= 0 and j < m:
        if matrix[i, j] == target:
            return True
        elif matrix[i, j] > target:
            i -= 1
        else:
            j += 1
    return False


if __name__ == '__main__':
    print(findNumberIn2DArray([
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ], 20))

