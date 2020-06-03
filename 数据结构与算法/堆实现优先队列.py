# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/3
desc: 树形结构实现优先队列（堆）
"""


class PrioQueue():
    """小元素优先"""
    def __init__(self, elist=[]):
        self._elem = list(elist)
        if elist:  # 如果elist非空，则创建小顶堆
            self.buildheap()

    def is_empty(self):
        return not self._elem

    def peek(self):
        """返回堆顶元素"""
        if self.is_empty():
            raise ValueError
        return self._elem[0]

    def enqueue(self, e):
        """入堆"""
        self._elem.append(None)  # 在尾端加入一个None，相当于创建一个空位
        self.siftup(e, len(self._elem))  # 向上筛选，找到e存放的位置（小元素优先）

    def siftup(self, e, last):
        """向上筛选"""
        i, j = last, (last - 1) // 2  # j为i所对应结点的父结点下标
        while i > 0 and e < self._elem[j]:  # 若父结点的元素大于e，说明e的优先级高于该父结点
            self._elem[i] = self._elem[j]  # 将父结点下移
            i, j = j, (j - 1) // 2  # 更新i，j（i相当于始终记录”空位“）
        self._elem[i] = e  # 跳出while循环说明e存放位置已找到

    def dequeue(self):
        """出堆"""
        if self.is_empty():
            raise ValueError
        e0 = self._elem[0]  # 拿出堆顶元素
        e = self._elem.pop()  # 拿出堆尾元素
        if len(self._elem) > 0:  # 若堆中元素大于1（因为前面刚弹出堆尾元素），向下筛选
            self.sifdown(e, 0, len(self._elem))
        return e0  # 返回堆顶元素

    def sifdown(self, e, begin, end):
        """向下筛选，目的是为了在堆顶元素弹出以后，将剩余的两个“子堆”合并成一个新堆"""
        i, j = begin, begin * 2 + 1  # j为i所对应结点的左子结点下标
        while j < end:
            if j + 1 < end and self._elem[j] > self._elem[j + 1]:  # 判断j和j+1两个兄弟结点的值哪个小，如果j+1结点小，则将j更新为j+1，否则j不变
                j += 1
            if e < self._elem[j]:  # 比较e和（j和j+1结点）中的较小者
                break  # 条件成立，说明e是三者中最小的，跳出循环
            self._elem[i] = self._elem[j]  # 将三者中最小值放到父节点的位置
            i, j = j, j * 2 + 1  # 更新i，j（i相当于始终记录”空位“）
        self._elem[i] = e

    def buildheap(self):
        """将所给可迭代对象创建为小顶堆"""
        end = len(self._elem)
        for i in range(end // 2, -1, -1):  # 从end//2开始，后面的元素都是满二叉树的叶结点，都可以看做为一个元素的堆，所以从此处往前一个一个建堆
            self.sifdown(self._elem[i], i, end)
