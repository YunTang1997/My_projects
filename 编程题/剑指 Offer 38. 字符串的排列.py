# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/7/23
desc: 输入一个字符串，打印出该字符串中字符的所有排列。你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
"""

def permutation(s):
    c, res = list(s), []
    def dfs(x):
        if x == (len(c) - 1):
            res.append("".join(c))
            return
        test = set()  # 用于减枝
        for i in range(x, len(c)):
            if c[i] in test:
                continue  # 重复，因此剪枝
            test.add(c[i])
            c[x], c[i] = c[i], c[x]  # 交换，将c[i]固定在第x位
            dfs(x + 1)  # 开启固定第x+1位字符
            c[x], c[i] = c[i], c[x]  # 恢复交换
    dfs(0)
    return res


if __name__ == "__main__":
    print(permutation("abc"))
    print(permutation("abb"))