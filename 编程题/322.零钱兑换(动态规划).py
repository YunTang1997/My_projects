# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/29
desc: 动态规划
"""


import sys


# 方法一：动态规划
def coinChange_1(coins, amount):
    # dp[i]表示利用所拥有硬币面值组合出面值为i的最少硬币数
    dp = [float('inf')] * (amount + 1)  # 由于相应面值最少硬币数，所以dp列表初始化为正无穷
    dp[0] = 0  # 面值为0时，不需要硬币

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


# 方法二：贪心算法
def coinChange_2(coins, amount):
    res, n = 0, len(coins)
    coins.sort(reverse=1)  # 将coins从大到小排序，贪心算法思想
    for i in range(n):
        if amount >= coins[i]:  # 优先选取大额硬币，使得所需硬币数目最少
            res += (amount // coins[i])
            amount %= coins[i]
    if amount == 0:  # 此时amount未0，说明有相应的硬币组合方案
        return res
    else:  # 没有组合方案
        return -1


if __name__ == '__main__':
    a = sys.stdin.readline().strip('[]\n').split(',')
    b = sys.stdin.readline()
    coins = list(map(int, a))
    amount = int(b)
    print(coinChange_1(coins, amount))
    print(coinChange_2(coins, amount))
