# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/29
desc: 动态规划
"""


import sys

class Solution():
    a = sys.stdin.readline().strip('[]\n').split(',')
    b = sys.stdin.readline()
    coins = list(map(int, a))
    amount = int(b)
    # print(coins)
    # print(amount)
    def coinChange(self, coins=coins, amount=amount):
        # dp[i]表示利用所拥有硬币面值组合出面值为i的最少硬币数
        dp = [float('inf')] * (amount + 1)  # 由于相应面值最少硬币数，所以dp列表初始化为正无穷
        dp[0] = 0  # 面值为0时，不需要硬币

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


print(Solution().coinChange())