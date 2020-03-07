def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
f()


# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数, f1()和f2()的调用结果互不影响
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
f1 == f2


# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# def count():
# #     fs = []
# #     for i in range(1, 4):
# #         def f():
# #             return i*i
# #         fs.append(f)
# #     return fs
# #
# #
# # f1, f2, f3 = count()
# # f1()
# # f2()
# # f3()


def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
f1()
f2()
f3()


def createCounter():
    def h():
        i = 0
        while True:
            i += 1
            yield i
    g = h()

    def counter():
        return next(g)
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')