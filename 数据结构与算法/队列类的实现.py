# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/13
desc: 队列类的实现
"""

class SQueue():
    def __init__(self, init_len=8):
        self._len = init_len  # 存储区的长度
        self._elems = [0] * init_len  # 元素储存
        self._head = 0  # 表头元素下标
        self._num = 0  # 元素个数

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if not self.is_empty():
            return self._elems[self._head]
        else:
            raise ValueError()

    def dequeue(self):
        if not self.is_empty():
            e = self._elems[self._head]
            self._head = (self._head + 1) % self._len
            self._num -= 1
            return e
        else:
            raise ValueError()

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1
