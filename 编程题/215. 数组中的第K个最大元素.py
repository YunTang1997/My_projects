# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/2
desc: 在未排序的数组中找到第k个最大的元素。请注意，你需要找的是数组排序后的第k个最大的元素，而不是第k个不同的元素。
"""


from timeit import timeit


# 利用快速排序（超出时间限制）
def quick_sort(alist, start, end):
    left, right = start, end
    if left >= right:
        return
    cur_elem = alist[left]
    while left < right:
        while left < right and alist[right] < cur_elem:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] >= cur_elem:
            left += 1
        alist[right] = alist[left]
    alist[left] = cur_elem
    quick_sort(alist, 0, left - 1)
    quick_sort(alist, left + 1, end)
    return alist


# 归并排序（通过）
def merge_sort(alist):
    n = len(alist)
    if n == 1:
        return alist
    mid = n // 2
    alist_left = alist[ : mid]
    alist_right = alist[mid : ]
    alist_left_sorted = merge_sort(alist_left)
    alist_right_sorted = merge_sort(alist_right)
    list_sorted = []
    letf_prev, right_prev = 0, 0
    while letf_prev < len(alist_left_sorted) and right_prev < len(alist_right_sorted):
        if alist_left_sorted[letf_prev] >= alist_right_sorted[right_prev]:
            list_sorted.append(alist_left_sorted[letf_prev])
            letf_prev += 1
        else:
            list_sorted.append(alist_right_sorted[right_prev])
            right_prev += 1
    list_sorted.extend(alist_left_sorted[letf_prev : ])
    list_sorted.extend(alist_right_sorted[right_prev : ])
    return list_sorted


def findKthLargest_1(nums, k):
    n = len(nums)
    quick_sort(nums, 0, n - 1)
    return nums[k - 1]


def findKthLargest_2(nums, k):
    n = len(nums)
    list_sorted = merge_sort(nums)
    return list_sorted[k - 1]


if __name__ == '__main__':
    print(findKthLargest_1([55, 26, 93, 97, 77, 31, 34, 55, 28], 1))
    print(timeit("findKthLargest_1([55, 26, 93, 97, 77, 31, 34, 55, 28], 1)", globals=globals(), number=1000))
    print(findKthLargest_2([55, 26, 93, 97, 77, 31, 34, 55, 28], 1))
    print(timeit("findKthLargest_2([55, 26, 93, 97, 77, 31, 34, 55, 28], 1)", globals=globals(), number=1000))
