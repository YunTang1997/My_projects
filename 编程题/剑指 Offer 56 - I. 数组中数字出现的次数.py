# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/7/11
desc: 一个整型数组nums里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""

from collections import Counter
from functools import reduce

def singleNumbers1(nums):
    numsCount = Counter(nums)
    res = []
    for key, value in numsCount.items():
        if value == 1:
            res.append(key)
    return res


def singleNumbers2(nums):
    res = set()
    for i in range(len(nums)):
        if nums[i] not in res:
            res.add(nums[i])
        else:
            res.remove(nums[i])
    return list(res)


def singleNumbers3(nums):
    yiHuoALL = reduce(lambda x, y: x ^ y, nums)
    mask = 1  # 通过 & 运算来判断一位数字不同即可分为两组
    while mask & yiHuoALL == 0:  # 为了方便操作，我们去寻找最低为的mask
        mask <<= 1
    a, b = 0, 0
    for i in nums:
        if i & mask == 0:
            a ^= i
        else:
            b ^= i
    return [a, b]


if __name__ == '__main__':
    print(singleNumbers1([4,1,4,6]))
    print(singleNumbers1([1,2,10,4,1,4,3,3]))
    print(singleNumbers2([4,1,4,6]))
    print(singleNumbers2([1,2,10,4,1,4,3,3]))
    print(singleNumbers3([4,1,4,6]))
    print(singleNumbers3([1,2,10,4,1,4,3,3]))
