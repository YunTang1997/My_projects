# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/19
desc: 验证回文字符串Ⅱ
"""


from timeit import timeit


def Validreverse(s):
    """判断是否是回文字符"""
    n = len(s)
    if n == 1:
        return True
    i, j = 0, n - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True  # 当s只有一个元素或while循环结束时，直接返回True


# 方法一：超出时间限制
def validPalindrome_1(s):
    n = len(s)
    if Validreverse(s):  # 不需要删除元素，本身就是回文字符
        return True
    for i in range(n):  # 逐个删除元素，看是否存在剩余子序列是回文字符的情况
        if i < n - 1:  # 处理边界情况
            s_new = s[0 : i] + s[i + 1: ]
        else:
            s_new = s[0 : i]
        if Validreverse(s_new):
            return True
    return False  # 当s只有一个元素时，直接返回True


# 方法二：贪心算法
def validPalindrome_2(s):
    n = len(s)
    i, j = 0, n - 1
    while i < j:
        if s[i] == s[j]:  # 两者相等进入下一次循环
            i += 1
            j -= 1
        else:  # 否则删除s[i]或者s[j]
            s_left = s[i : j]  # 删除元素s[j]
            s_right = s[i + 1 : j + 1]  # 删除元素s[i]
            if Validreverse(s_left) or Validreverse(s_right):  # 只要两者中有一个是回文字符串即可
                return True
            else:
                return False
    return True  # 当s只有一个元素时，直接返回True


if __name__ == '__main__':
    print(validPalindrome_1("abbca"))
    print(timeit("validPalindrome_1('abbca')", globals=globals(), number=10000))
    print(validPalindrome_2("abbca"))
    print(timeit("validPalindrome_2('abbca')", globals=globals(), number=10000))



