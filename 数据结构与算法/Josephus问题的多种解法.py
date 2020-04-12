# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/12
desc: Josephus问题的多种解法
"""

from 循环单链表类 import LClist
import time


def Josephus_A(n, k, m):
    """
    基于“数组概念的解法”
    :param n: 总共多少个人
    :param k: 从第几个人开始
    :param m: 数到几会被移出队伍
    :return: 顺序输出各出列人的编号
    """

    people = list(range(1, n + 1))  # 生成所需人数队列
    i = k - 1  # 从第k个人开始

    for num in range(n):  # 每一次大循环必出列一个人，所以循环n次
        count = 0  # 每出列一个人重新报数
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")  # 数到m，输出此人编号
                people[i] = 0  # 取值为0，代表此人出列
            i = (i + 1) % n  # 保证下标i在合理的范围内
        if num < n - 1:
            print(", ", end="")
        else:
            print("")
    return


Josephus_A(n=30, k=7, m=9)


def Josephus_L(n, k, m):
    """
    基于顺序表的解
    :param n: 总共多少个人
    :param k: 从第几个人开始
    :param m: 数到几会被移出队伍
    :return: 顺序输出各出列人的编号
    """

    people = list(range(1, n + 1))
    num, i = n, k - 1

    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i),
              end=(", " if num > 1 else "\n"))
    return


Josephus_L(n=30, k=7, m=9)


class Josephus(LClist):  # 创建LClist的子类
    def turn(self, i):
        for i in range(i):
            self._rear = self._rear.next

    def __init__(self, n, k, m):  # 初始化子类
        LClist.__init__(self)  # 继承基类的全部属性和方法
        for i in range(n):  # 通过尾端插入的方式，创建人数为n的循环队列
            self.append(i + 1)

        self.turn(k - 1)  # 从第k个人开始

        while not(self.is_empty()):
            self.turn(m - 1)
            print(self.pop(),
                  end=("\n" if self.is_empty() else ", "))


test = Josephus(n=30, k=7, m=9)
