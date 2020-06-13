# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/13
desc: 给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那两个整数，并返回他们。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""


def twoSum(nums, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 1):
        if nums[i] > target:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = n - 1
        while i < j:
            cur_sum = nums[i] + nums[j]
            if cur_sum > target:
                j -= 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif cur_sum < target:
                i += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
            else:
                res.extend([nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    return res


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
