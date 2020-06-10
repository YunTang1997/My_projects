# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/10
desc: 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
"""


import re


def isPalindrome(s):
    if not s:  # 空串为有效字符串
        return True
    s = s.lower()  # 将所有字符变成小写
    tmp_list = re.split('\W', s)  # 以所有非字符数字字符为分割条件，分割s，并返回一个列表
    s_split = ''.join(tmp_list)  # 以空字符串为连接字符将tmp_list组合为一个字符串
    n = len(s_split)
    i, j = 0 ,n - 1
    while i < n and j >= 0:
        if s_split[i] != s_split[j]:
            return False
        i, j = i + 1, j - 1
    return True


if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))