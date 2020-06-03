# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/3
desc:堆排序
"""


def heap_sort(alist):
    """堆排序"""
    def siftdown(alist, e, start, end):
        """为了使得最终排序的结果由小到大，采用大顶堆"""
        i, j = start, 2 * start + 1
        while j < end:
            if j + 1 < end and alist[j] < alist[j + 1]:
                j += 1
            if e > alist[j]:
                break
            alist[i] = alist[j]
            i, j = j, 2 * j + 1
        alist[i] = e

    end = len(alist)
    for i in range(end // 2, -1, -1):  # 将所给列表生成大顶堆
        siftdown(alist, alist[i], i, end)

    for i in range(end - 1, 0, -1):
        e = alist[i]  # 拿出堆尾元素，相当于将下标为i的位置空出
        alist[i] = alist[0]  # 将堆顶元素放到下标为i的位置，同时也相当于将堆顶的位置空出
        siftdown(alist, e, 0, i)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 34, 55, 20]
    heap_sort(alist)
    print(alist)

