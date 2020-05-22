# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/21
desc: 希尔排序
"""


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:  # gap变化到0之前，插入算法执行的次数
        for i in range(gap, n):  # 插入排序算法，与普通插入排序算法的区别就是gap长度
            j = i
            while j >= gap:
                if alist[j - gap] > alist[j]:
                    alist[j - gap], alist[j] = alist[j], alist[j - gap]
                    j -= gap
                else:
                    break
        gap //= 2  # 缩短gap的步长
    return alist


if __name__ == '__main__':
    print(shell_sort([54, 26, 93, 17, 77, 31, 34, 55, 20]))
