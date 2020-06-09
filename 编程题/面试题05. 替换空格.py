# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/9
desc: 请实现一个函数，把字符串s中的每个空格替换成"%20"
"""


import re


def replaceSpace_1(s):
    res = re.sub(' ', '%20', s)
    return res


def replaceSpace_2(s):
    res = ''
    for i in s:
        if i != " ":
            res += i
        else:
            res += "%20"
    return res


if __name__ == '__main__':
    print(replaceSpace_1("We are happy."))
    print(replaceSpace_2("We are happy."))
