# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/31
desc: 对称二叉树
"""


from collections import deque  # deque双端队列


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None


    def add(self, elem):
        """以广度遍历的形式在二叉树中找到适当的位置并插入元素"""
        Node = TreeNode(elem)  # 创建插入的结点
        if self.root is None:
            self.root = Node
            return
        queue = deque()  # 创建双端队列
        queue.append(self.root)  # 每次添加元素都应该让根结点进队
        while queue:  # 当队列非空的时候
            cur_node = queue.popleft()  # 左端弹出元素
            if cur_node.left is None:
                cur_node.left = Node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = Node
                return
            else:
                queue.append(cur_node.right)

    def clear(self):
        """清空二叉树"""
        self.root = None


# 方法一（递归）
def isSymmetric_1(root):
    """
    判断AB两个根结点当前节点值是否相等
    判断A结点的右子树与B结点的左子树是否对称
    判断A结点的左子树与B结点的右子树是否对称
    :param root: 根结点
    :return: bool
    """
    if root is None:  # 空树判断为对称
        return True
    def mirror(root_left, root_right):
        if root_left is None and root_right is None:  # 递归终止条件，当两者为None时，返回True
            return True
        elif root_left is None or root_right is None:  # 递归终止条件，当其中一者为None时，返回False
            return False
        elif root_left.value != root_right.value:  # 递归终止条件，当两者值不相等时，返回False
            return False
        return mirror(root_left.left, root_right.right) and mirror(root_left.right, root_right.left)  # 递归调用
    return mirror(root.left, root.right)


# 方法二（将递归转化为迭代，利用缓存结构代替递归）
def isSymmetric_2(root):
    if root is None:  # 空树判断为对称
        return True
    queue = deque([])  # 创建双端队列
    queue.extend([root.left, root.right])  # 将根结点的左右结点加入队列
    while queue:
        root_left = queue.popleft()  # 左端弹出第一个元素
        root_right = queue.popleft()  # 右端弹出第二个元素
        if root_left is None and root_right is None:
            continue  # 注意是continue，当两者均为None时直接弹出队列即可
        elif root_left is None or root_right is None:  # 当其中一者为None时，返回False
            return False
        elif root_left.value != root_right.value:  # 当两者值不相等时，返回False
            return False
        queue.extend([root_left.left, root_right.right, root_left.right, root_right.left])
    return True  # 当二叉树的结点全部被检查（queue变为空），说明对称



if __name__ == '__main__':
    alist = [1,2,2,3,4,4,3]
    binarytree = BinaryTree()
    for i in range(len(alist)):
        binarytree.add(alist[i])
    print(isSymmetric_1(binarytree.root))

    binarytree.clear()
    alist = [1,2,2,None,3,None,3]
    for i in range(len(alist)):
        binarytree.add(alist[i])
    print(isSymmetric_1(binarytree.root))

    binarytree.clear()
    alist = [1,2,2,3,4,4,3]
    for i in range(len(alist)):
        binarytree.add(alist[i])
    print(isSymmetric_2(binarytree.root))

    binarytree.clear()
    alist = [1,2,2,None,3,None,3]
    for i in range(len(alist)):
        binarytree.add(alist[i])
    print(isSymmetric_2(binarytree.root))











