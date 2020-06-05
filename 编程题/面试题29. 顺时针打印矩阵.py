# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/5
desc: 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
"""


import numpy as np

def spiralOrder(matrix):
    if not matrix:  # 处理空矩阵的情况
        return []
    matrix = np.mat(matrix)
    row = matrix.shape[0]  # 矩阵的行数
    # row = len(matrix)  # 没有利用np，得到普通矩阵的行数
    col = matrix.shape[1]  # 矩阵的列数
    # col = len(matrix[0])  # 没有利用np，得到普通矩阵的列数
    left, right, top, bottom, res = 0, col - 1, 0, row - 1, []  # 创建左右上下边界值以及res
    while True:  # 按从左到右，从上到下，从右到左，从下到上顺时针循环
        for i in range(left, right + 1):
            res.append(matrix[top, i])
        top += 1  # 每输出完第一行，则top加1
        if top > bottom:  # 满足该条件说明输出完毕
            break
        for i in range(top, bottom + 1):
            res.append(matrix[i, right])
        right -= 1  # 每输出完最后一列，则right减1
        if left > right:  # 满足该条件说明输出完毕
            break
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom, i])
        bottom -= 1  # 每输出完最后一行，则bottom减1
        if top > bottom:  # 满足该条件说明输出完毕
            break
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i, left])
        left += 1  # 每输出完第一列，则left加1
        if left > right:  # 满足该条件说明输出完毕
            break
    return res


if __name__ == '__main__':
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))





