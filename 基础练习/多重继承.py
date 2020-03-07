class A(object):
    def foo(self):
        print('A foo')

    def bar(self):
        print('A foo')


class B(object):
    def foo(self):
        print('B foo')

    def bar(self):
        print('B bar')


class C1(A, B):
    pass


class C2(A, B):
    def bar(self):
        print('C2-bar')


class D(C1, C2):
    pass


if __name__ == '__main__':
    print(D.__mro__)  # 多重继承顺序，C3算法（拓扑排序）
    d = D()
    d.foo()
    d.bar()


