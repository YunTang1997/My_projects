# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/25
desc: LRU缓存机制
"""


class Node():
    """定义一个结点"""
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache():
    def __init__(self, capacity):
        self._capacity = capacity
        self._hashmap = {}  # 定义一个哈希表，其中存储{key：结点地址}
        self._head = Node()  # 定义头结点
        self._tail = Node()  # 定义尾结点
        #  将头结点和尾结点连起来，形成双链表
        self._head.next = self._tail
        self._tail.prev = self._head


    def node_move_to_tail(self, key):
        """hashma中key所对应的结点，移到尾结点之前，代表该节点的数据最新使用"""
        node = self._hashmap[key]  # 将key所对应的结点拿出
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self._tail  # 将key所对的结点移到尾结点之前
        node.prev = self._tail.prev
        self._tail.prev.next = node
        self._tail.prev = node


    
    def get(self, key):
        if key in self._hashmap:  # 如果key在hashmap中已存在，则将其移至尾结点之前，代表最新使用
            self.node_move_to_tail(key)
        res = self._hashmap.get(key, -1)  # key存在则返回对应结点，不存在返回-1
        if res == -1:
            return -1
        else:
            return res.value  # 注意若key存在则返回的是一个结点


    def put(self, key, value):
        if key in self._hashmap:  # 如果key在hashmap中已存在，则将其移至尾结点之前，代表最新使用，并将对应结点的值更新
            self.node_move_to_tail(key)
            self._hashmap[key].value = value
        else:
            if len(self._hashmap) == self._capacity:  # 容量已满
                self._hashmap.pop(self._head.next.key)  # 将头结点后面的结点弹出，因为它最久未使用
                self._head.next = self._head.next.next
                self._head.next.prev = self._head
            new = Node(key=key, value=value)  # 容量未满，直接创建一个新结点
            self._hashmap[key] = new  # 并将该新结点存入hashmap中
            # 将新结点放到尾结点之前，代表最新使用
            new.next = self._tail
            new.prev = self._tail.prev
            self._tail.prev.next = new
            self._tail.prev = new


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))


