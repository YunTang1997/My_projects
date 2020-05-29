# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/29
desc: 打家劫舍
"""


# 方法一
def rob_1(nums):
    n = len(nums)
    if n == 0:  # 若nums为空列表，则返回0
        return 0
    dp = [0] * n  # dp[i]表示前i个房间，在第i个房间必选的情况下，小偷可以获得的最大金额
    for i in range(n):
        if i == 0 or i == 1:
            dp[i] = nums[i]
        else:
            dp[i] = max(dp[0 : i - 1]) + nums[i]
    return max(dp)


# 方法二
def rob_2(nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [0] * n  # dp[i]表示前i个房间小偷可以获得的最大金额
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])  # 第i个房间选与不选有两种情况，选择金额较多的情况
    return dp[-1]

if __name__ == '__main__':
    print(rob_1([2, 1, 1, 2]))
    print(rob_2([2, 1, 1, 2]))
