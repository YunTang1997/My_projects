# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/3
desc: 最大子序和
"""

from timeit import timeit


# 方法一(超时)
def maxSubArray1(nums):
    n = len(nums)
    positve = [i for i in range(n) if nums[i] > 0]
    m = len(positve)
    ans = max(nums)
    for i in positve:
        for j in range(i, n):
            ans = max(sum(nums[i : j + 1]), ans)
    return ans

print(maxSubArray1([-2,1,-3,4,-1,2,1,-5,4]))
print(timeit("maxSubArray1([-2,1,-3,4,-1,2,1,-5,4])", globals=globals(), number=1000))


# 方法二动态规划
def maxSubArray2(nums):
    n = len(nums)
    max_value = set()  # 记录以第i位结尾的连续子数组最的大和
    max_value.add(nums[0])
    pre = nums[0]
    for i in range(1, n):
        pre = max(pre + nums[i], nums[i])  # 判断第i位元素是否加入前一个子序列（转移方程）
        max_value.add(pre)
    return max(max_value)  # 取所有值中的最大值


print(maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
print(timeit("maxSubArray2([-2,1,-3,4,-1,2,1,-5,4])", globals=globals(), number=1000))