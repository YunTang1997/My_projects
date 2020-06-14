# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/13
desc: 给你一个包含n个整数的数组nums，判断nums中是否存在三个元素a，b，c ，使得a + b + c = 0请你找出所有满足条件且不重复的三元组。注意：答案中不可以包含重复的三元组。
"""


def quick_sort(nums, start, end):
    left, right = start, end
    if left >= right:
        return
    cur_elem = nums[left]
    while left < right:
        while left < right and cur_elem <= nums[right]:
            right -= 1
        nums[left] = nums[right]
        while left < right and cur_elem > nums[left]:
            left += 1
        nums[right] = nums[left]
    nums[left] = cur_elem
    quick_sort(nums, start, left - 1)
    quick_sort(nums, left + 1, end)
    return nums


def threeSum(nums):
    n = len(nums)
    nums = quick_sort(nums, 0, n - 1)  # 将原来数组从小到大排序
    res = []
    for i in range(n - 2):  # 注意最大只能取到n - 3
        if nums[i] > 0:  # 当目标值target>=0时，才能使用该判断语句优化代码，若target为负值则不可以
            break
        if i > 0 and nums[i] == nums[i - 1]:  # 跳过相同的结果集
            continue
        left, right = i + 1, n - 1  # 定义双指针
        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]  # 三数之和
            if cur_sum > 0:  # 若三数之和大于目标值，则说明右指针需要往左移
                right -= 1
                while left < right and nums[right] == nums[right + 1]:  # 若右指针更新之后所代表的值和之前一致，则继续左移
                    right -= 1
            elif cur_sum < 0:  # 若三数之和小于目标值，则说明做指针需要往右移
                left += 1
                while left < right and nums[left] == nums[left - 1]:  # 若左指针更新之后所代表的值和之前一致，则继续右移
                    left += 1
            else:  # 否则找到了符合题意的结果
                res.append([nums[i], nums[left], nums[right]])
                left += 1  # 更新左指针的值
                right -= 1  # 更新右指针的值
                while left < right and nums[left] == nums[left - 1]: # 若左指针更新之后所代表的值和之前一致，则继续右移，消除重复解
                    left += 1
                while left < right and nums[right] == nums[right + 1]: # 若右指针更新之后所代表的值和之前一致，则继续左移，消除重复解
                    right -= 1
    return res


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([0, 0, 0, 0]))





