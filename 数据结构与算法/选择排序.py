# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/21
desc: 选择排序
"""


def select_sort(alist):
    n = len(alist)
    for i in range(n - 1):
        min_index = i  # min_index记录最小值的下标
        for j in range(i + 1, n):  # 找到最小值
            if alist[min_index] > alist[j]:
                min_index = j  # 更新最小值所对应的下标
        alist[i], alist[min_index] = alist[min_index], alist[i]  # 将找到的最小元素放到正确的位置
    return alist


if __name__ == '__main__':
    print(select_sort([54, 26, 93, 17, 77, 31, 34, 55, 20]))
    print(select_sort([1, 2, 3, 4, 0, -1, -2, 10, 9]))


