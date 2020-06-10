# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/10
desc: 斐波那契数列
"""


# 方法一（迭代法）
def fib_1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        res = a + b
        a, b = b, res
    return res


# 方法二（递归）
def fib_2(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fib_2(N - 1) + fib_2(N - 2)


if __name__ == '__main__':
    print(fib_1(10))
    print(fib_2(10))
