# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/15
desc: 二叉树类的实现
"""

class SQueue(object):
    def __init__(self, init_len):
        self._len = init_len
        self._elems = [0] * self._len
        self._head = 0
        self._num = 0

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


    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1


class Node(object):
    def __init__(self, elem):
        self._elem= elem
        self._left = None
        self._right = None


class Bintree(object):
    def __init__(self):
        self._root = None

    def add(self, elem):
        node = Node(elem)
        if self._root is None:
            self._root = node
            return
        queue = SQueue(init_len=8)
        queue.enqueue(self._root)
        while not queue.is_empty():  # 注意条件的表达
            cur_node = queue.dequeue()
            if cur_node._left is None:
                cur_node._left = node
                return
            else:
                queue.enqueue(cur_node._left)
            if cur_node._right is None:
                cur_node._right = node
                return
            else:
                queue.enqueue(cur_node._right)

    def breath_travel(self):
        """广度遍历"""
        if self._root is None:
            return
        queue = SQueue(init_len=8)
        queue.enqueue(self._root)
        while not queue.is_empty():  # 注意条件的表达
            cur_node = queue.dequeue()
            print(cur_node._elem, end=" ")
            if cur_node._left is not None:
                queue.enqueue(cur_node._left)
            if cur_node._right is not None:
                queue.enqueue(cur_node._right)

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node._elem, end=" ")
        self.preorder(node._left)
        self.preorder(node._right)


    def midorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.midorder(node._left)
        print(node._elem, end=" ")
        self.midorder(node._right)


    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node._left)
        self.postorder(node._right)
        print(node._elem, end=" ")


if __name__ == '__main__':
    bt = Bintree()
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)
    bt.breath_travel()
    print()
    bt.preorder(bt._root)
    print()
    bt.midorder(bt._root)
    print()
    bt.postorder(bt._root)





