# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/21
desc: python中栈数据结构的两种基本实现方式
"""


from 循环单链表类 import LNode


# 定义异常类
class StackUnderfolw(ValueError):
    pass


# 栈的顺序表实现
class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self.is_empty():
            raise StackUnderfolw("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        return self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderfolw("in SStack.pop()")
        return self._elems.pop()


# 栈的链接表实现
class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self.is_empty():
            raise StackUnderfolw("in LStack.top()")
        return self._top.elem


    def push(self, elem):
        self._top = LNode(elem, next_=self._top)


    def pop(self):
        if self.is_empty():
            raise StackUnderfolw("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem



if __name__ == '__main__':

    st1 = SStack()
    # st1.top()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())

    st2 = LStack()
    # st2.top()
    st2.push(7)
    st2.push(8)
    while not st2.is_empty():
        print(st2.pop())




