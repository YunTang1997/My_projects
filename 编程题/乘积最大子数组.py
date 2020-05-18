# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/18
desc: 乘积最大子数组(注意和最大子序和比较其中的差别)
"""


from timeit import timeit

def maxProduct_1(nums):
    n = len(nums)
    max_i, min_i = set(), set()  # 记录以nums[i]结尾的连续子数组乘积的最大值、最小值
    max_i.add(nums[0])
    min_i.add(nums[0])
    pre_max, pre_min = nums[0], nums[0]  # 以nums[i]结尾的连续子数组乘积的最大值、最小值的中间变量
    for i in range(1, n):
        current = (pre_max * nums[i], pre_min * nums[i], nums[i])  # 由于乘积会出现负负得正的情况，所以以元素nums[i]结尾的最小乘积也需要记录下来
        pre_max, pre_min = max(current), min(current)
        max_i.add(pre_max)
        min_i.add(pre_min)
    return max(max_i)


def maxProduct_2(nums):
    """
    dp[i][j]：以nums[i]结尾的连续子数组的最值，计算最大值还是最小值由j来表示，j就两个值；
    当 j = 0的时候，表示计算的是最小值；
    当 j = 1的时候，表示计算的是最大值
    """
    n = len(nums)
    dp = [[nums[0] for _ in range(2)] for _ in range(n)]
    for i in range(1, n):
        #  状态转移方程，以nums[i]正负区分情况
        if nums[i] >= 0:
            dp[i][0] = min(nums[i], dp[i - 1][0] * nums[i])
            dp[i][1] = max(nums[i], dp[i - 1][1] * nums[i])
        else:
            dp[i][0] = min(nums[i], dp[i - 1][1] * nums[i])
            dp[i][1] = max(nums[i], dp[i - 1][0] * nums[i])

    res = dp[0][1]
    for i in range(1, n):
        res = (res if res >= dp[i][1] else dp[i][1])
    return res


if __name__ == '__main__':
    print(maxProduct_1([-4, 5, -2]))
    print(timeit("maxProduct_1([-4, 5, -2])", globals=globals(), number=1000))
    print(maxProduct_2([-4, 5, -2]))
    print(timeit("maxProduct_2([-4, 5, -2])", globals=globals(), number=1000))
