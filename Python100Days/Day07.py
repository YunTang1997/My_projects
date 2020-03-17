# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/16
desc: 字符串和常用数据结构
"""


import sys


# 生成式和生成器
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in "ABCDE" for y in "1234567"]
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(f"生成式占用内存数：{sys.getsizeof(f)}")  # 查看对象占用内存的字节数
print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(f"生成器占用内存数：{sys.getsizeof(f)}")  # 相比生成式生成器不占用存储数据的空间
print(f)
# for val in f:
#     print(val)


# 集合
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print("Length=", len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# 向集合添加元素和从集合删除元素
print(set4)
set1.add(4)
print(set1)
set1.add(5)
print(set1)
set2.update([11, 12])
print(set2)
set2.discard(5)
print(set2)
# 集合的成员、交集、并集、差集等运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

# 字典
# 创建字典的字面量语法
scores = {"唐韵": 97, "白元芳": 78, "狄仁杰": 82}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(["a", "b", "c"], "123"))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# for key in scores:
#     print(f"{key}: {scores[key]}")
scores.update(冷面=67, 方启鹤=85)
print(scores)
print(scores.get("武则天"))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get("武则天", 60))
# 删除字典中的末尾元素，并返回元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop("唐韵", 100))
print(scores)