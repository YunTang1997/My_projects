# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/28
desc: 动态规划
"""


class Solution:
    def waysToChange(self, n):
        coins=[1, 5, 10, 25]
        return self.change(n, coins) % 1000000007

    def change(self, amount, coins):
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        print(dp)
        # dp[i][j]的含义：
        # j代表所需要金额
        # i代表选到几种硬币，如i=0代表一种硬币都不用，i=1代表用coins[:1]类硬币（即只用coins[0]）,i=2代表用coins[:2]类硬币（即只用coins[0],coins[1]）,以此类推
        # 初始化状态
        for c in range(1, amount + 1):
            dp[0][c] = 0  # 没有任何一种硬币，不论需要多少金额，都没有对应的方案数
        for r in range(len(coins) + 1):
            dp[r][0] = 1  # 如果金额为0，对多少种硬币来说都是1种方案

        for r in range(1, len(coins) + 1):
            for c in range(1, amount + 1):
                dp[r][c] = dp[r - 1][c]  # 不选当前指标r对应的硬币
                if c >= coins[r - 1]:
                    dp[r][c] += dp[r][c - coins[r - 1]]  # 选当前指标r对应的硬币
        return dp[-1][-1]

print(Solution().waysToChange(5))