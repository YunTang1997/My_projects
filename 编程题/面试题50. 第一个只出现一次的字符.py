# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/9
desc: 在字符串s中找出第一个只出现一次的字符。如果没有，返回一个单空格。s只包含小写字母。
"""


from collections import Counter


def firstUniqChar(s):
    res = ' '
    if s == '':
        return res
    s_counter = Counter(s)  # 统计s中每个元素出现的次数
    for i in s:
        if s_counter[i] == 1:  # 寻找第一个出现并且为一次的字符
            res = i
            break
    return res


if __name__ == '__main__':
    print(firstUniqChar("abaccdeff"))
    print(firstUniqChar(""))

