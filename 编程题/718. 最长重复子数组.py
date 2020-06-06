# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/5
desc: 给两个整数数组A和B，返回两个数组中公共的、长度最长的子数组的长度。
"""


from collections import defaultdict


# 暴力法（超出时间限制）
def findLength_1(A, B):
    n, m = len(A), len(B)
    B_dict = defaultdict(int)
    res = 0
    for index, value in enumerate(B):
        B_dict[value] = index
    for index, value in enumerate(A):
        for value in B_dict:
            k = 0
            while index + k < n and B_dict[value] + k < m and A[index + k] == B[B_dict[value] + k]:
                k += 1
            res = max(res, k)
    return res


# 动态规划
def findLength_2(A, B):
    n, m = len(A), len(B)
    # dp[i][j]代表A[ : i]和B[ : j]的最长公共子数组的长度，公共子数组必须以A[i-1]和B[j-1]结尾
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] != B[j - 1]:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            res = max(res, dp[i][j])
    return res


# 动态规划
def findLength_3(A, B):
    n, m = len(A), len(B)
    # dp[i][j]代表A[i : ]和B[j : ]最长公共前缀的长度
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    res = 0
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if A[i] != B[j]:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i+1][j+1] + 1
        res = max(res, dp[i][j])
    return res


if __name__ == '__main__':
    print(findLength_1([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(findLength_2([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(findLength_3([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))


