# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/13
desc: 迷宫的回溯法求解
"""


class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if not self.is_empty():
            return self._elems[-1]
        else:
            raise ValueError()

    def push(self, e):
        return self._elems.append(e)

    def pop(self):
        if not self.is_empty():
            return self._elems.pop()
        else:
            raise ValueError()


