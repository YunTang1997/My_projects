# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/13
desc: 字符串朴素匹配算法
"""


def naive_match(t, p):
    """
    字符串朴素匹配算法
    :param t: 目标串
    :param p: 模式串
    :return: 返回模式串在目标串中匹配成功的起始、终止下标
    """

    if not isinstance(t, str) and not isinstance(p, str):
        raise TypeError

    m = len(p)
    n = len(t)
    j = 0
    result = []  # 结果

    while j < n:  # 将目标串匹配完
        i = 0
        while i < m and j < n:  # 当i=m时匹配成功
            if p[i] == t[j]:  # 该对字符相同，考虑下一对字符
                i, j = i + 1, j + 1
            else:
                i, j = 0, j - i + 1  # 该对字符不相同，模式串往右移动一格，重新开始匹配
        if i == m:
            result.append([j - i, j - i + m - 1])  # 返回模式串在目标串中匹配成功的起始、终止下标

    return result  # 返回结果


if __name__ == '__main__':
    print(naive_match(t="zbcde", p="ce"))
    print(naive_match(t="zbcdefgcdeq", p="cde"))
