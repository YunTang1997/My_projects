# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/27
desc: 利用移动窗口和哈希表（字典）解决无重复最长子串的问题
"""


from timeit import timeit
from collections import defaultdict

# 方法一
class Solution:
    def lengthOfLongestSubstring_1(self, s):
        s_len = len(s)
        s_dict = {}
        for key, elem in enumerate(s):  # 将原字符串转化为索引：元素的字典，方便后面元素访问
            s_dict[key] = elem

        hasmap = {}  # 利用哈希表处理匹配过的字符
        # i为移动窗口的开始位置，j为移动窗口的结束位置
        i, j, ans= 0, 0, 0
        while i <= s_len and j <= s_len:  # 注意边界值的处理
            if j < s_len and s_dict[j] not in hasmap.keys():  # 前后两个判断条件顺序不能更改，否则s_dict[j]索引溢出
                hasmap[s_dict[j]] = j  # 将键值对加入字典
                j += 1  # 更新j值
            else:
                ans = max(ans, j - i)  # 得到符合要求的子串长度
                if j < s_len:  # 限定j的范围
                    if hasmap.get(s_dict[j]) >= i:  # 注意判断hasmap中重复键值与i的关系
                        i = hasmap.get(s_dict[j]) + 1  # 更新i的值（移动窗口）
                    hasmap[s_dict[j]] = j  # 更新hasmap中重复元素的值
                j += 1  # 更新j值
        return ans


# 方法二
def lengthOfLongestSubstring_2(s):
    n = len(s)
    occ = set()
    ans, j = 0, -1

    for i in range(n):
        if i != 0:  # i不为0说明滑动窗口起点向右移动了，则需要删除set中处于滑动窗口左侧的元素
            occ.remove(s[i - 1])
        while (j + 1) < n and s[j + 1] not in occ:
            occ.add(s[j + 1])
            j += 1
        ans = max(ans, j - i + 1)
    return ans


# 方法三
def lengthOfLongestSubstring_3(s):
    n = len(s)
    lookup = defaultdict(int)
    left, right = 0, 0
    max_len = 0
    count = 0  # count=0代表没有元素重复
    while right < n:
        if lookup[s[right]] > 0:
            count += 1  # count=1代表有元素重复
        lookup[s[right]] += 1
        right += 1
        while count > 0:
            if right - left - 1 > max_len:
                max_len = right - left
            if lookup[s[left]] > 1:  # 若s[left]是重复的元素
                count -= 1
            lookup[s[left]] -= 1
            left += 1
    return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring_1("pwwkew"))
    print(timeit("Solution().lengthOfLongestSubstring_1('pwwkew')", globals=globals(), number=1000))
    print(lengthOfLongestSubstring_2("pwwkew"))
    print(timeit("lengthOfLongestSubstring_2('pwwkew')", globals=globals(), number=1000))
    print(lengthOfLongestSubstring_3("pwwkew"))
    print(timeit("lengthOfLongestSubstring_3('pwwkew')", globals=globals(), number=1000))





