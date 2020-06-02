# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/2
desc: 求1+2+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
"""


res = 0
def sumNums_1(n):
    global res  # 创建全局变量res
    n > 1 and sumNums_1(n - 1)  # 利用and的短路效应，代替递归中会出现if的情况，如果n>1成立，就会递归否则跳出递归
    res += n
    return res


def sumNums_2(n):
    if n == 1:
        return 1
    n += sumNums_2(n - 1)
    return n

if __name__ == '__main__':
    print(sumNums_1(10))
    print(sumNums_2(10))