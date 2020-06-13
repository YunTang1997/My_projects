# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/12
desc: 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字x的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出-1。
"""


def nextGreaterElements_1(nums):
    n = len(nums)
    res =[-1 for _ in range(n)]
    stack = []
    for i in range(2 * n):
        while stack and nums[i % n] > nums[stack[-1]]:
            '''if res[stack[-1]] == -1:  # 没有更新过的值需要更新
                res[stack.pop()] = nums[i % n]
            else:  # 更新过的值不需要再更新
                stack.pop()'''
            res[stack.pop()] = nums[i % n]
        stack.append(i % n)
    return res


def nextGreaterElements_2(nums):
    n = len(nums)
    res = [-1 for _ in range(n)]
    stack = []
    for i in range(2 * n - 1, -1, -1):
        while stack and nums[i % n] >= nums[stack[-1]]:
            stack.pop()
        if stack:
            res[i % n] = nums[stack[-1]]
        stack.append(i % n)
    return res


if __name__ == '__main__':
    print(nextGreaterElements_1([1,2,1]))
    print(nextGreaterElements_1([73, 74, 75, 71, 69, 72, 76, 73]))
    print(nextGreaterElements_1([100, 1, 11, 1, 120, 111, 123, 1, -1, -100]))
    print(nextGreaterElements_2([1,2,1]))
    print(nextGreaterElements_2([73, 74, 75, 71, 69, 72, 76, 73]))
    print(nextGreaterElements_2([100, 1, 11, 1, 120, 111, 123, 1, -1, -100]))
