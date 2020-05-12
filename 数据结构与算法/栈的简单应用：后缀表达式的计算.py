# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/11
desc: 后缀表达式的计算
"""

import sys


class ESStack(object):
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def depth(self):
        return len(self._elems)

    def top(self):
        if self.is_empty():
            raise ValueError("in SStack.top()")
        else:
            return self._elems[-1]

    def push(self, elems):
        return self._elems.append(elems)

    def pop(self):
        if self.is_empty():
            raise ValueError("in SStack.pop()")
        else:
            return self._elems.pop()


def suf_exp_evaluaor(exp):
    operators = "+-*/"
    st = ESStack()

    for i in exp:
        if i not in operators:
            st.push(float(i))
            continue

        else:
            if st.depth() < 2:
                raise SyntaxError("Short of operand(s)")
            else:
                a = st.pop()
                b = st.pop()
                if i == "+":
                    c = b + a
                elif i == "-":
                    c = b - a
                elif i == "*":
                    c = b * a
                elif i == "/":
                    if a != float(0):
                        c = b / a
                    else:
                        raise ZeroDivisionError()
                st.push(c)
    if st.depth() == 1:
        return st.pop()
    else:
        raise SyntaxError("Extra operand(s)")


if __name__ == '__main__':
    line = sys.stdin.readline().strip().split()
    print(suf_exp_evaluaor(exp=line))

