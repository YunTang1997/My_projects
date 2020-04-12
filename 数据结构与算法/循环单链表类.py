# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/12
desc: 循环单链表类
"""


class LNode():  # 简单的表结点类
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LClist():  # 循环单链表
    def __init__(self):
        self._rear = None  # 建立一个空表

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):  # 表头插入元素
        p = LNode(elem)  # 创建一个表结点实例p
        if self._rear is None:  # 如果是一个空表
            p.next = p  # 建立一个结点环
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):  # 尾端插入
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):  # 前端弹出
        if self._rear is None:  # 如果是空表
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next  # 表头结点
        if p is self._rear:  # 如果只有一个结点
            self._rear = None
        else:
            self._rear.next = p.next  # 删除表头结点
        return p.elem

    def printall(self):  # 输出表元素
        if self.is_empty():
            return
        else:
            p = self._rear.next
            while p is not self._rear:
                return p.elem
                p = p.next
