# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/13
desc: 给定一个包含n个整数的数组nums和一个目标值target，判断nums中是否存在四个元素a，b，c和d，使得a+b+c+d的值与target相等?找出所有满足条件且不重复的四元组。注意：答案中不可以包含重复的四元组。
"""


def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 3):
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j - 1] == nums[j]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if cur_sum > target:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
    return res


if __name__ == '__main__':
    print(fourSum([1, 0, -1, 0, -2, 2], 0))
    print(fourSum([0, 0, 0, 0], 0))
    print(fourSum([1,-2,-5,-4,-3,3,3,5], -11))


