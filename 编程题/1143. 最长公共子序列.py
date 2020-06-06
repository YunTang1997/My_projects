# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/6
desc: 最长公共子序列
"""


def longestCommonSubsequence(text1, text2):
    n, m = len(text1), len(text2)
    # dp[i][j]表示text1[ : i]和text[ : j]的最长公共子序列（text1[i -1]可选可不选，text2[j - 1]可选可不选），则dp[-1][-1]就是答案
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] != text2[j - 1]:  # 当两者不相等的时候，说明两者有一个不在公共子序中，或两个都不在
                # dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = dp[i-1][j-1] + 1
    return dp[-1][-1]


if __name__ == '__main__':
    print(longestCommonSubsequence("abcde", "ace"))
    print(longestCommonSubsequence("abc", "abc"))
    print(longestCommonSubsequence("abc", "def"))
