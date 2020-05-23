# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/23
desc: 至多包含两个不同字符的最长子串
"""

from collections import defaultdict


def lengthOfLongestSubstringTwoDistinct(s):
    n = len(s)
    lookup = defaultdict(int)
    right, left = 0, 0
    max_len = 0
    count = 0
    while right < n:
        if lookup[s[right]] == 0:
            count += 1
        lookup[s[right]] += 1
        right += 1
        while count > 2:
            if lookup[s[left]] == 1:
                count -= 1
            lookup[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left)
    return max_len