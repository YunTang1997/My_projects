# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/19
desc: 冒泡排序
"""


def bubble_sort(alist):
    n = len(alist)
    for i in range(n - 1):  # 每循环一次找到一个位置，则循环n-1次，就可以将长度为n的列表全部排序
        count = 0
        for j in range(n - 1 - i):  # 注意每次内层循环结束下标
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        if count == 0:  # 如果第一次内层循环以后，并没有发生前后元素交换，则说明alist本身有序，直接返回即可
            return alist
    return alist


if __name__ == '__main__':
    print(bubble_sort([54, 26, 93, 17, 77, 31, 34, 55, 20]))
    print(bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]))




