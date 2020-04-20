# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/17
desc: 列表转化为字符串的两种方式
"""

a = ['a', 'b', 'd', 'c', 'r', 'f', 'a', 's', 'q']

# 第一种方式
b = "".join(a)  # 可以选择你需要的连接符
print(b)


# 第二种方式
c = ""
for i in b:
    c = c + i
print(c)
