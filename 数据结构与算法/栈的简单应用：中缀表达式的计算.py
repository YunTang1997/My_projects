# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/21
desc: 中缀表达式的计算
"""

import sys


class EEStack():
    def __init__(self):
        self._elems = []
    
    def is_empty(self):
        return self._elems == []
    
    def depth(self):
        return len(self._elems)
    
    def top(self):
        if not self.is_empty():
            return self._elems[-1]
        else:
            raise ValueError()

    def push(self, elems):
        return self._elems.append(elems)
    
    def pop(self):
        if not self.is_empty():
            return self._elems.pop()
        else:
            raise ValueError()


priority = {"(" : 1, "+": 3, "-": 3, "*": 5, "/": 5}
infix_operators = "+-*/()"


def token(line):
    i, llen = 0, len(line)
    while i < llen:
        """当遇到空格的时候"""
        while i < llen and line[i].isspace():
            i += 1
        if i >= llen:
            break
        """运算符的情况"""
        if line[i] in infix_operators:
            yield line[i]
            i += 1
            continue

        """运算对象的情况"""
        j = i + 1
        while j < llen and not line[j].isspace() and line[j] not in infix_operators:
            """处理负指数"""
            if ((line[j] == 'e' or line[j] == 'E') and j + 1 < llen and line[j + 1] == '-'):
                j += 1
            j += 1
        yield line[i : j]
        i = j


def trans_infix_suffix(line):
    st = EEStack()
    exp = []

    for i in token(line):
        if i not in infix_operators:
            exp.append(i)
        elif st.is_empty() or i == "(":
            st.push(i)
        elif i == ")":
            while not st.is_empty() and st.top() != "(":
                exp.append(st.pop())
            if st.is_empty():
                raise SyntaxError("Missing '('.")
            st.pop()  # 弹出左括号，右括号也不进栈
        else:
            while (not st.is_empty()) and priority[st.top()] >= priority[i]:
                exp.append(st.pop())
            st.push(i)

    while not st.is_empty():
        if st.top() == "(":
            raise SyntaxError("Extra '('.")
        else:
            exp.append(st.pop())

    return exp


def suf_exp_evaluator(exp):
    opeartors = "+-*/"
    st = EEStack()

    for i in exp:
        if i not in opeartors:
            st.push(float(i))
            continue
        else:
            if st.depth() < 2:
                raise SyntaxError()
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
        raise SyntaxError()


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    exp = trans_infix_suffix(line)
    print(suf_exp_evaluator(exp))



    

