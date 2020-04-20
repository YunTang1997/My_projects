# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/15
desc: 投票计数(华为)
"""


import sys
import re
from collections import Counter  #　计数


def count(name_list):  # 得到姓名以及票数
    name_list_new = name_list
    name_list_new = list(set(name_list_new))  # 将列表转化为集合，去掉相同的名字

    name_num = []
    for i in range(len(name_list_new)):
        num = 0
        for j in range(len(name_list)):
            if name_list_new[i] == name_list[j]:
                num += 1
        name_num.append([name_list_new[i], num])

    name_num = dict(name_num)

    return name_num


def mingri(name_list):
    # input_ = count(name_list)
    input_ = Counter(name_list)  # 元素以字典key的形式存储，并将其计数存储为字典value

    input_keys = sorted(input_.keys())
    input_sort1 = []
    for i in input_keys:
        input_sort1.append([i, input_[i]])
    input_sort1 = dict(input_sort1)

    input_values = input_.values()
    result = []
    for key, elem in zip(input_sort1.keys(), input_sort1.values()):
        if elem == max(input_values):
            result.append(key)

    result = sorted(result)

    return result[0]


if __name__ == '__main__':
    a = sys.stdin.readline()
    b = a.strip().split(',')

    first_elem = re.compile("[A-Z]")  # 创建检验输入首字母的正则表达式对象
    other_elems = re.compile("[a-z]+")  #　创建检验除了首字母之外部分的正则表达式对象

    go_on = True  # 控制输出

    if 0 < len(b) < 100:
        for i in b:
            if not(first_elem.search(i, 0, 1) and other_elems.search(i, 1)):  # 判断是否输入值均为首字母大写、其余字母小写
                print("error.0001")
                go_on = False
                break
    else:
        print("error.0001")
        go_on = False

    if go_on:
        print(mingri(b))



