# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/10
desc: 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""


def isPalindrome(x):
    if x < 0:
        return False
    x_str = str(x)
    n = len(x_str)
    i, j = 0, n - 1
    while i < n and j >= 0:
        if x_str[i] != x_str[j]:
            return False
        i, j = i + 1, j - 1
    return True


if __name__ == '__main__':
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))
