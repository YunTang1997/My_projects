# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/13
desc: 154.寻找旋转排序数组中的最小值II
"""


def findMin(nums):
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right -= 1
    return nums[left]


if __name__ == '__main__':
    print(findMin([1,3,5]))
    print(findMin([2,2,2,0,1]))
