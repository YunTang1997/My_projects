# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/15
desc: 函数参数作用域
"""

def foo():
    b = "hello"  # 对于foo()函数，b属于局部作用域；对于内置函数bar()函数，b属于嵌入作用域，bar()可以调用它；在foo()之外不可调用

    def bar():
        c = True  # 对于bar()函数，c属于局部作用域，在bar()函数之外不可调用
        print(a)
        print(b)
        print(c)

    bar()


if __name__ == '__main__':
    a = 100  # 全局作用域
    foo()
