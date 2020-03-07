#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__  # 使得用print和直接显示变量结果一致


# print(Student('Micheal'))  # 调用的是__str__()

# s = Student('Micheal')
# s  # 调用的是__repr__()


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # __iter__()方法，该方法返回一个迭代对象

    def __next__(self):  # 利用__next__()方法，返回下一个值
        t = (self.b, self.a + self.b)
        self.a = t[0]
        self.b = t[1]  # 以上三步等价于 self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        else:
            return self.a

    def __getitem__(self, n):  # 利用__getitem__()方法，表现得像list那样按照下标取出元素， 且可以使用切片
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for j in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if step:
                    if x >= start and (x - start) % step == 0:
                        L.append(a)
                else:
                    if x >= start:
                        L.append(a)
                a, b = b, a + b
            return L
        else:
            pass


# for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
for i in Fib():
    print(i)

f = Fib()
f[0:10:2]

