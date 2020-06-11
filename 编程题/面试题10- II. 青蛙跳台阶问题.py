# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/11
desc: 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


#  该题可以和面试题46.把数字翻译成字符串进行对比


def numWays(n):
    # dp[i]表示上一个i级台阶有多少种跳法
    dp = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # 考虑第i和i-1级台阶，是两级台阶一起跳，还是分两次跳
    return dp[-1]


if __name__ == '__main__':
    print(numWays(2))
    print(numWays(7))
