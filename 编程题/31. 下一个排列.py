# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/13
desc: 31.下一个排列
"""


# 同556.下一个更大的元素III

# 单调栈
def nextPermutation(nums):
    stack, n = [], len(nums)
    stack.append(nums.pop())
    while nums and stack[-1] <= nums[-1]:
        stack.append(nums.pop())
    if not nums:
        return stack
    for i in range(len(stack)):
        if stack[i] > nums[-1]:
            stack[i], nums[-1] = nums[-1], stack[i]
            break
    nums += stack
    return nums


if __name__ == '__main__':
    print(nextPermutation([1, 2, 3]))
    print(nextPermutation([3, 2, 1]))
    print(nextPermutation([1, 1, 5]))


