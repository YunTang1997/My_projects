import functools


# def int2(x, base=2):
#     return int(x, base)
#
#
# print(int2('1000000'))


# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=2)
int2('1000000')


sorted2 = functools.partial(sorted, key=abs)

sorted2([-5, 1, 4, -2, 3])
# 相当于
kw = {'key': abs}
sorted([-5, 1, 4, -2, 3], **kw)


# partial(func,*args,**kw),func是必须要传入的，而且至少需要一个args或是kw参数
def add(a, b, c):
    return a + b + c


p = functools.partial(add, 12)
p(1, 2)
p(2, 3)
p(3, 4)