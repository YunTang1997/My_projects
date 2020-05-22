# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/22
desc: 从中序与后序遍历构造二叉树
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




class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:  # 这里要返回结点，而不是返回具体的数
        return TreeNode(inorder[0])
    hasmap = {values: i for i, values in enumerate(inorder)}  # 创建中序{值：索引}
    root = TreeNode(postorder[-1])  # 后序遍历最后一个值为根节点
    root_index = hasmap[root.val]  # 获得根结点在中序遍历中的索引值
    root.left = buildTree(inorder[ : root_index], postorder[: root_index])  # 构建左子树
    root.right = buildTree(inorder[root_index + 1 : ], postorder[root_index : -1])  # 构建右子树
    return root


def breath_travel(inorder, postorder):
    root = buildTree(inorder, postorder)
    if root is None:
        return None
    queue = SQueue(init_len=8)
    queue.enqueue(root)
    while not queue.is_empty():
        cur_node = queue.dequeue()
        print(cur_node.val, end=" ")
        if cur_node.left is not None:
            queue.enqueue(cur_node.left)
        if cur_node.right is not None:
            queue.enqueue(cur_node.right)


if __name__ == '__main__':
    print(breath_travel([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))

