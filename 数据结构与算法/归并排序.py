# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/24
desc: 归并排序
"""


def merge_sort(alist):
    n = len(alist)
    # 当所给列表只有一个元素的时候，直接返回本身即可
    if n <= 1:
        return alist
    """以下为归并排序中“分”的部分"""
    # 以mid为界限将alist分为两个部分
    mid = n // 2
    # alist_left为左半部分
    alist_left = alist[ : mid]
    # alist_right为右半部分
    alist_right  = alist[mid : ]
    # 对左半部分进行递归，并将排好序的左半部分命名为sorted_left
    sorted_left = merge_sort(alist_left)
    # 对右半部分进行递归，并将排好序的右半部分命名为sorted_right
    sorted_right = merge_sort(alist_right)
    """以下为归并排序中“合”的部分"""
    # 分别给左右两个部分定义两个指针prev_left， prev_right
    prev_left, prev_right = 0, 0
    # 创建一个空列表，储存排好序的列表
    sorted_alist = []
    # 当两个指针均在有效范围内时，将两者中所指的较小元素放入sorted_alist中
    while prev_left < len(sorted_left) and prev_right < len(sorted_right):
        if sorted_left[prev_left] <= sorted_right[prev_right]:
            sorted_alist.append(sorted_left[prev_left])
            prev_left += 1
        else:
            sorted_alist.append(sorted_right[prev_right])
            prev_right += 1
    # 当跳出while循环时，将sorted_left 、sorted_right中还没有放入sorted_alist的元素放入sorted_alist中
    # 由于sorted_left 、sorted_right中元素本身有序，直接将剩余部分放入sorted_alist即可
    sorted_alist += sorted_left[prev_left : ]
    sorted_alist += sorted_right[prev_right : ]
    # 返回当前排序结果
    return sorted_alist


if __name__ == '__main__':
    print(merge_sort([54, 26, 93, 17, 77, 31, 34, 55, 20]))


