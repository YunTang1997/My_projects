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


def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):  # 右边无序序列中会有多少个元素被取出
        for j in range(i, 0, -1):  # 从右边的无序序列中取出第一个元素，即i的位置的元素，然后将其插入到左边有序序列正确的位置中
            if alist[j - 1] > alist[j]:
                alist[j - 1], alist[j] = alist[j], alist[j - 1]
            else:  # 优化算法
                break
    return alist


if __name__ == '__main__':
    print(list_sort([1, 2, 3, 4, 0, -1, -2, 10, 9]))
    print(insert_sort([1, 2, 3, 4, 0, -1, -2, 10, 9]))
