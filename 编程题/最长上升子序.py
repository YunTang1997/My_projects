# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/18
desc: 最长上升子序
"""


def lengthOfLIS(nums):
    """
    dp[i]表示以nums[i]结尾的「上升子序列」的长度。注意：这个定义中nums[i]必须被选取，且必须是这个子序列的最后一个元素。
    """
    n = len(nums)
    if n == 0:
        return 0
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    res = max(dp)
    return res


if __name__ == '__main__':
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))