# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/23
desc:
"""

from collections import defaultdict


def lengthOfLongestSubstringKDistinct(s, k):
    lookup = defaultdict(int)
    start = 0
    end = 0
    max_len = 0
    count = 0
    while end < len(s):
        if lookup[s[end]] == 0:
            count += 1
        lookup[s[end]] += 1
        end += 1
        while count > k:
            if lookup[s[start]] == 1:
                count -= 1
            lookup[s[start]] -= 1
            start += 1
        max_len = max(max_len, end - start)
    return max_len
