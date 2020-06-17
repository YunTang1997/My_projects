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


def longestCommonPrefix_1(strs):
    if not strs:
        return ""
    prefix, m = strs[0], len(strs)
    for i in range(1, m):
        prefix = commonprefix(prefix, strs[i])
        if not prefix:  # 如果某次两者的公共前缀为空，则说明strs所有字符串的公共前缀为空
            break
    return prefix


# 方法二（纵向扫描）
def longestCommonPrefix_2(strs):
    if not strs:
        return ""
    strs_len = list(map(len, strs))
    n = min(strs_len)  # 最长公共前缀的长度肯定<=strs中最短的字符串长度
    m = len(strs)
    tmp = True  # “开关”
    prefix = ""
    for i in range(n):
        cur_str = strs[0][i]
        for j in range(1, m):
            if cur_str != strs[j][i]:
                tmp = False
                break
        if tmp:
            prefix += cur_str
        else:
            return prefix
    return prefix


# 方法三
def longestCommonPrefix_3(strs):
    """利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀"""
    if not strs:
        return ""
    s = list(map(set, zip(*strs)))
    # print(s)
    prefix = ""
    for i in s:
        i_list = list(i)
        if len(i) > 1:
            break
        prefix += i_list[0]
    return prefix


if __name__ == '__main__':
    print(longestCommonPrefix_1(["flower","flow","flight"]))
    print(longestCommonPrefix_1(["dog","racecar","car"]))
    print(longestCommonPrefix_2(["flower","flow","flight"]))
    print(longestCommonPrefix_2(["dog","racecar","car"]))
    print(longestCommonPrefix_3(["flower","flow","flight"]))
    print(longestCommonPrefix_3(["dog","racecar","car"]))


