# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/2
desc: 输入整数数组arr，找出其中最小的k个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
"""


def quick_sort(alist, start, end):
    """快速排序"""
    left, right = start, end
    if left >= right:
        return
    cur_elem = alist[left]
    while left < right:
        while left < right and alist[right] >= cur_elem:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < cur_elem:
            left += 1
        alist[right] = alist[left]
    alist[left] = cur_elem
    quick_sort(alist, start, left - 1)
    quick_sort(alist, left + 1, end)
    return alist


def getLeastNumbers(arr, k):
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    return arr[ : k]


if __name__ == '__main__':
    print(getLeastNumbers([55, 26, 93, 97, 77, 31, 34, 55, 28], 4))


