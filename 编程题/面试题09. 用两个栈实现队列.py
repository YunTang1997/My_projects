# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/10
desc: 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail和deleteHead，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead操作返回-1)
"""


# 栈无法实现队列功能：栈底元素（对应队首元素）无法直接删除，需要将上方所有元素出栈。
# 双栈可实现列表倒序：设有含三个元素的栈 A=[1,2,3]和空栈B=[]。若循环执行A元素出栈并添加入栈B，直到栈A为空，则A=[], B=[3,2,1]，即栈B元素实现栈A元素倒序。
# 利用栈BB删除队首元素：倒序后，B执行出栈则相当于删除了A的栈底元素，即对应队首元素。


class CQueue:
    def __init__(self):
        self._A_stack = []  # A栈用于储存元素
        self._B_stack = []  # B栈将A栈中元素颠倒，使得原来处于栈底的元素处于栈顶

    def appendTail(self, value):
        self._A_stack.append(value)

    def deleteHead(self):
        if self._A_stack or self._B_stack:  # 两者中至少一个非空
            if self._B_stack:  # 若B栈非空，只要弹出B栈的栈顶元素
                return self._B_stack.pop()
            while self._A_stack:  # 当B栈为空而A栈非空的时候，将A栈元素全部以倒序放入B栈中
                self._B_stack.append(self._A_stack.pop())
            return self._B_stack.pop()  # 弹出B栈栈顶元素
        else:  # 两者全空，说明此时CQueue中没有元素，返回-1
            return -1