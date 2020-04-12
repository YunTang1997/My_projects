# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/12
desc: 插入排序（从小到大）
"""


def list_sort(lst):
    if not isinstance(lst, list):
        raise TypeError
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j - 1] > x:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x  # 补足最后一个元素

    return lst


print(list_sort([1, 2, 3, 4, 0, -1, -2, 10, 9]))
