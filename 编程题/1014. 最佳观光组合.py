# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/17
desc: 最佳观光组合
"""


def maxScoreSightseeingPair(A):
    n = len(A)
    pre_max = A[0] + 0
    res = 0
    for i in range(1, n):
        res = max(res, pre_max + A[i] - i)
        pre_max = max(pre_max, A[i] + i)
    return res


if __name__ == '__main__':
    print(maxScoreSightseeingPair([8,1,5,2,6]))