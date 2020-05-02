# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/27
desc: 利用移动窗口和哈希表（字典）解决无重复最长子串的问题
"""


from timeit import timeit

# 方法一
class Solution:
    def lengthOfLongestSubstring(self, s):
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


print(Solution().lengthOfLongestSubstring("abba"))
print(timeit("Solution().lengthOfLongestSubstring('abba')", globals=globals(), number=1000))


# 方法二
def lengthOfLongestSubstring(s):
    n = len(s)
    occ = set()
    ans, j = 0, -1

    for i in range(n):
        if i != 0:
            occ.remove(s[i - 1])
        while (j + 1) < n and s[j + 1] not in occ:
            occ.add(s[j + 1])
            j += 1
        ans = max(ans, j - i + 1)

    return ans

print(lengthOfLongestSubstring("abba"))
print(timeit("lengthOfLongestSubstring('abba')", globals=globals(), number=1000))


