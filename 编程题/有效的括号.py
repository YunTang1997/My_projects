# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/18
desc: 有效的括号
"""

class Stack(object):
    """创建一个栈类"""
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if not self.is_empty():
            return self._elems[-1]
        else:
            raise ValueError

    def push(self, elem):
        return self._elems.append(elem)

    def pop(self):
        if not self.is_empty():
            return self._elems.pop()
        else:
            raise ValueError


def isValid(s):
    if s  == "":  # 空串情况
        return True
    parens = "([{"
    opposite = {')': '(', ']': '[', '}': '{'}
    stack = Stack()  # 生成一个栈
    n = len(s)
    for i in range(n):
        if s[i] in parens:  # 如果s[i]存在于parens，将其压入栈
            stack.push(s[i])
        else:
            if not stack.is_empty() and opposite[s[i]] == stack.pop():  # 如果stack不为空，且括号对应正确
                res = True
            else:
                return False
    if not stack.is_empty():  # 此时若stack非空，意味着还有剩余的parens未匹配
        return False
    return res

if __name__ == '__main__':
    print(isValid("["))


