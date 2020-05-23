# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/23
desc: 最小覆盖子串
"""


from collections import Counter
from collections import defaultdict  # defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值


# 方法一
def minWindow_1(s, t):
    n = len(s)
    need = Counter(t)
    window = Counter()  # 生成一个Counter对象，是dict的一个子类，默认值为0，注意dict本身不具有默认值
    left, right = 0, 0
    min_len, res = float('inf'), ''
    while right < n:
        window[s[right]] += 1  # 将窗口右端遍历过的元素以{值：出现次数}的形式存入Counter对象中
        right += 1  # 扩大窗口
        #  all()函数用于判断给定的可迭代参数iterable中的所有元素是否都为TRUE，如果是返回True，否则返回False。元素除了是0、空、None、False外都算True。
        #  all()函数判断空元组、空列表返回值为True，这里要特别注意。
        while all(map(lambda x: window[x] >= need[x], need.keys())):  # 当移动窗口window中t各个元素出现的次数大于或等于t本身中的次数时
            if right - left < min_len:
                res = s[left : right]
                min_len = right - left
            window[s[left]] -= 1
            left += 1  # 缩小窗口
    return res


# 方法二
def minWindow_2(s, t):
    n = len(s)
    lookup = defaultdict(int)
    for value in t:
        lookup[value] += 1
    min_len = float('inf')
    left, right ,res = 0, 0, ''
    counter = len(t)  # 记录窗口元素和t中元素的差值
    while right < n:
        if lookup[s[right]] > 0:
            counter -= 1
        lookup[s[right]] -= 1
        right += 1
        while counter == 0:
            if right - left < min_len:
                min_len = right - left
                res = s[left : right]
            if lookup[s[left]] == 0:
                counter += 1
            lookup[s[left]] += 1
            left += 1
    return res


if __name__ == '__main__':
    print(minWindow_1("ADOBECODEBANC", "ABC"))
    print(minWindow_2("ADOBECODEBANC", "ABC"))
    print(minWindow_2("a", "aa"))


