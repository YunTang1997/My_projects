# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/4
desc: 给你一个长度为n的整数数组nums，其中n>1，返回输出数组output，其中output[i]等于nums中除nums[i]之外其余各元素的乘积。
"""


from functools import reduce
from timeit import timeit


# 方法一（超时）
def productExceptSelf_1(nums):
    n = len(nums)
    res = []
    for i in range(n):
        res.append(reduce(lambda x, y:x*y, nums[ : i] + nums[i+1 : ]))
    return res


# 方法二
def productExceptSelf_2(nums):
    n = len(nums)
    res = [1] * n
    right = 1  # 计算后缀累计乘积
    for i in range(n - 1, -1, -1):
        right *= nums[i]
        res[i] = right
    left = 1  # 计算前缀累计乘积
    for i in range(n - 1):
        res[i] = left * res[i + 1]  # 除去第i个位置，剩余元素的乘积=左边所有元素的乘机*右边元素所有元素的乘机
        left *= nums[i]
    res[-1] = left  # 填充最后一个元素
    return res


if __name__ == '__main__':
    print(productExceptSelf_1([1, 2, 3, 4]))
    print(timeit("productExceptSelf_1([1, 2, 3, 4])", globals=globals(), number=1000))
    print(productExceptSelf_2([1, 2, 3, 4]))
    print(timeit("productExceptSelf_2([1, 2, 3, 4])", globals=globals(), number=1000))
