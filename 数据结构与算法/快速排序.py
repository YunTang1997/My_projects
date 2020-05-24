# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/24
desc: 快速排序
"""


def quick_sort(alist, start, end):
    # 定义双指针
    left, right = start, end
    # 递归终止条件
    if left >= right:
        return
    # cur_value记录当前排序元素（相当于把left指向的位置空出来）
    cur_value = alist[left]
    # 循环条件
    while left < right:
        # 指针right左移条件，第二个判断条件取等是为了将列表中与cur_value相等的元素均放在列表的一侧
        while left < right and alist[right] >= cur_value:
            right -= 1
        # 跳出while循环，说明此时right所指向的元素小于cur_value，所以将alist[right]放到left所指向的位置
        alist[left] = alist[right]
        # 指针left右移条件，第二个判断条件不取等（因为前一个while循环包含了等号）
        while left < right and alist[left] < cur_value:
            left += 1
        # 跳出while循环，说明此时left所指向的元素大于或等于cur_value，所以将alist[left]放到right所指向的位置
        alist[right] = alist[left]
    # 跳出大while循环（left == right），说明已找到cur_value该放置的位置
    alist[left] = cur_value
    # 对cur_value左边的列表进行快排
    quick_sort(alist, start, left - 1)
    # 对cur_value右边的列表进行快排
    quick_sort(alist, left + 1, end)
    # 返回排好序的alist
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 34, 55, 20]
    print(quick_sort(alist, 0, len(alist) - 1))
