# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/14
desc: 1300.转变数组后最接近目标值的数组和
"""


import bisect  # 用于[有序序列]的插入和查找
# 查找：bisect(array, item)
# 插入：insort(array,item)
# 使用bisect.insort，比bisect先查找该插入哪个位置，再用insert方法插入更加快速的方法
# bisect还有bisect_left，insort_left的用法，和不带left的用法的区别是：当插入的元素和序列中的某一个元素相同时，该插入到该元素的前面（左边，left），还是后面（右边）；如果是查找，则返回该元素的位置还是该元素之后的位置。
# bisect.bisect和bisect.bisect_right一样


# 方法一（暴力法，超出时间限制）
def findBestValue_1(arr, target):
    max_value = max(arr)
    res, tmp_abs = 0, target
    for i in range(1, max_value + 1):
        cur_list = []
        for j in arr:
            cur_list.append(min(i, j))
            cur_abs = abs(sum(cur_list) - target)
        if cur_abs < tmp_abs:
            res = i
            tmp_abs = cur_abs
    return res


# 方法二（暴力法通过二分查找优化）
def findBestValue_2(arr, target):
    arr.sort()
    n = len(arr)
    max_arr = arr[-1]
    # 注意34~36得到一个序列前缀和的方法，此处求前缀和是为了方便后面求的修改以后的arr数组和
    prefix_sum = [0]
    for i in arr:
        prefix_sum.append(prefix_sum[-1] + i)
    res, diff = 0, target
    for i in range(1, max_arr + 1):  # 注意这个循环范围的由来
        prev = bisect.bisect_left(arr, i)
        cur_sum = prefix_sum[prev] + (n - prev) * i
        if abs(cur_sum - target) < diff:  # 遍历完for循环以后，res肯定是满足条件且最小的，因为i是从小到达遍历的
            res = i
            diff = abs(cur_sum - target)
    return res


if __name__ == '__main__':
    print(findBestValue_1([4,9,3], 10))
    print(findBestValue_1([2,3,5], 10))
    print(findBestValue_1([60864,25176,27249,21296,20204], 56803))
    print(findBestValue_2([4,9,3], 10))
    print(findBestValue_2([2,3,5], 10))
    print(findBestValue_2([60864,25176,27249,21296,20204], 56803))


