# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/24
desc: 二分查找
"""


from timeit import timeit


def binary_search_1(alist, search_item):
    """
    递归版本（仅查找元素是否存在）
    :param alist: 查找列表（注意！注意！alist必须有序）
    :param search_item: 查找元素
    :return:
    """
    n = len(alist)
    mid = n // 2
    if n > 0:
        if alist[mid] == search_item:
            return True
        elif alist[mid] < search_item:
            return binary_search_1(alist[mid + 1:], search_item)
        else:
            return binary_search_1(alist[: mid], search_item)
    return False


def binary_search_2(alist, search_item, start, end):
    """
    递归版本（查找的元素在列表中是否存在，若存在返回对应下标）
    :param alist: 查找列表（注意！注意！alist必须有序）
    :param search_item: 查找元素
    :param start: 查找范围起始位置
    :param end: 查找范围终止位置
    :return: 查找的元素在列表中是否存在，若存在返回对应下标
    """
    if start <= end:
        mid = (start + end) // 2
        if alist[mid] == search_item:
            return (True, mid)
        elif alist[mid] < search_item:
            return binary_search_2(alist, search_item, mid + 1, end)
        else:
            return binary_search_2(alist, search_item, start, mid - 1)
    return (False,)


def binary_search_3(alist, search_item):
    """
    非递归版本（查找的元素在列表中是否存在，若存在返回对应下标）
    :param alist: 查找列表（注意！注意！alist必须有序）
    :param search_item: 查找元素
    :return: 查找的元素在列表中是否存在，若存在返回对应下标
    """
    n = len(alist)
    start, end = 0, n - 1
    # 当start>end的时候，相当于所查找的列表为空，则跳出循环
    while start <= end:
        # 将所查找的列表以mid为界一分为二
        mid = (start + end) // 2
        # 找到需要的值，直接返回
        if alist[mid] == search_item:
            return True, mid
        # 当alist[mid] < search_item时说明需要的值在alist[mid + 1 :
        # ]中（因为alist本身从小到大有序），所以更新start
        elif alist[mid] < search_item:
            start = mid + 1
        # 当alist[mid] > search_item时说明需要的值在alist[start :
        # mid]中（因为alist本身从小到大有序），所以更新end
        else:
            end = mid - 1
    # 查找完alist都没有找到需要的元素，返回False
    return False


if __name__ == '__main__':
    alist = [17, 20, 26, 31, 34, 54, 55, 77, 93]
    print(binary_search_1(alist, 55))
    print(binary_search_1(alist, 1000))
    print(timeit("binary_search_1(alist, 55)", globals=globals(), number=1000))

    print(binary_search_2(alist, 55, 0, len(alist) - 1))
    print(binary_search_2(alist, 1000, 0, len(alist) - 1))
    print(timeit("binary_search_2(alist, 55, 0, len(alist) - 1)", globals=globals(), number=1000))

    print(binary_search_3(alist, 55))
    print(binary_search_3(alist, 1000))
    print(timeit("binary_search_3(alist, 55)", globals=globals(), number=1000))
