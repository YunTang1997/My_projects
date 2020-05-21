# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/16
desc: 最长回文子串
"""

from timeit import timeit

# 方法一（动态规划）
def longestPalindrome_1(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]  # dp[i][j]代表串s[i : j + 1]是否是回文串

    for i in range(n):  # 当只有一个字符的时候肯定是回文串
        dp[i][i] == True

    ans = [0, 1]  # 初始化回文子串的起始索引为0和回文子串的长度为1，注意长度初始化为1处理s为单个字符的情况
    for j in range(1, n):
        for i in range(j):
            # if ((j + 1) - i) <= 3 and s[j] == s[i]
            if (j - i) <= 2:
                if s[i] == s[j]:  # 当子串的长度<=3时，只需要判断头尾两个字符是否相等，就可判别是否是回文串
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                if s[i] == s[j] and dp[i + 1][j - 1] == True:  # 当子串长度>3时，状态转移
                    dp[i][j] = True
                else:
                    dp[i][j] = False

            if dp[i][j]:  # 记录回文子串的起始索引和子串长度
                if (j - i + 1) > ans[1]:
                    ans = [i, j - i + 1]
    return s[ans[0] : (ans[0] + ans[1])]


#  方法二（中心扩散法）
def __center_spread(s, n, left, right):
        """
        left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
        """
        i, j = left, right
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
        return s[(i + 1) : j], j - i - 1

def longestPalindrome_2(s):
    n = len(s)
    if n < 2:
        return s

    max_len, res = 1, s[0]
    for i in range(n):
        palindrome_odd, odd_len = __center_spread(s, n, i, i)
        palindrome_even, even_len = __center_spread(s, n, i, i + 1)

        cur_max_sub = (palindrome_odd if odd_len >= even_len else palindrome_even)
        if len(cur_max_sub) > max_len:
            max_len = len(cur_max_sub)
            res = cur_max_sub
    return res


if __name__ == '__main__':
    print(longestPalindrome_1("abdba"))
    print(timeit("longestPalindrome_1('abdba')", globals=globals(), number=1000))

    print(longestPalindrome_2("abdba"))
    print(timeit("longestPalindrome_2('abdba')", globals=globals(), number=1000))






