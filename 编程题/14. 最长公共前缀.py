# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/16
desc: 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
"""


# 方法一（横向扫描）
def commonprefix(str1, str2):
    """返回str1和str2两个字符串最长公共前缀"""
    index, n = 0, min(len(str1), len(str2))
    while index < n and str1[index] == str2[index]:
        index += 1
    return str1[ : index]


def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix, m = strs[0], len(strs)
    for i in range(1, m):
        prefix = commonprefix(prefix, strs[i])
        if not prefix:
            break
    return prefix


if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))

