# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/9
desc: 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
"""

# num_to_str = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', \
#                   12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', \
#                   23: 'x', 24: 'y', 25: 'z'}


def translateNum(num):
    num_str = str(num)
    n = len(num_str)
    if n == 1:
        return 1
    # dp[i]表示num前i个元素组成的数字有几种组合方式
    dp = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        if 10 <= int(num_str[i - 2] + num_str[i - 1]) <= 25:  # 当倒数两个数能组成[10, 25]之间的数字时，注意要大于等于10
            dp[i] = dp[i - 1] + dp[i - 2]  # dp[i]由dp[i-1]和dp[i-2]转移得到
        else:
            dp[i] = dp[i - 1]
    return dp[-1]


if __name__ == '__main__':
    print(translateNum(12258))
    print(translateNum(1))
    print(translateNum(122))
    print(translateNum(2047483648))



