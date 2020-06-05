# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/3
desc: 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字
"""


from collections import Counter


def findRepeatNumber_1(nums):
    n = len(nums)
    finded = set()
    for i in range(n):
        if nums[i] in finded:
            return nums[i]
        else:
            finded.add(nums[i])


def findRepeatNumber_2(nums):
    nums_counter = Counter(nums)
    for key, value in nums_counter.items():
        if value > 1:
            return key


if __name__ == '__main__':
    print(findRepeatNumber_1([2, 3, 1, 0, 2, 5, 3]))
    print(findRepeatNumber_2([2, 3, 1, 0, 2, 5, 3]))