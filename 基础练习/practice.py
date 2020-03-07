import math
import functools
import time
from collections import Iterable
from collections import Iterator
from _functools import reduce
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

'ABC'.encode('ascii')
'中文'.encode('UTF-8')

b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('UTF-8')

b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')

# 'Hello, %s' % 'word'
# 'Hi, %s, you have $%d.' % ('Michael', 1000000)
#
# '%2d-%02d' % (3, 1)
# '%.2f' % 3.145926
#
# 'growth rate: %d %%' % 7

s1 = 72
s2 = 85
r = (s2 - s1) / s1
print('小明提升的百分点: %.1f' % r)

# 以下定义相当于数字1，并不是含有一个元素的元组
# t = (1)
# 定义只有一个元素的元组
# t = (1, )

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

height = 17.5
weight = 80.5
bmi = weight / height ** 2

if bmi > float(32):
    print('严重肥胖')
elif 32 >= bmi > 28:
    print('肥胖')
elif 28 >= bmi > 25:
    print('过重')
elif 25 >= bmi > 18.5:
    print('正常')
else:
    print('过轻')

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello, %s!' % name)

# 只打印10以内的奇数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

# 交集与并集操作
# set集合中的元素只能是不可变元素（list可变，整数和字符串是不可变的）
# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print(s1 | s2)

# a = 'abc'
# print(a.replace('a', 'A'))
# print(a)

str_list = ['a', 'a', 'b', 'a', 'b', 'c']
setA = set(str_list)

dictB = {}
for i in setA:
    dictB[i] = str_list.count(i)
print(dictB)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


my_abs('a')

isinstance('a', int)


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)
print(r)


def quadratic(a, b, c):
    sq = b ** 2 - 4 * a * c
    if a == 0:
        return -c / b
    elif sq < 0:
        print("无解")
    else:
        x1 = ((-b) + math.sqrt(sq)) / (2 * a)
        x2 = ((-b) - math.sqrt(sq)) / (2 * a)
        return x1, x2


print('quadratic(2, 3, 1)=', quadratic(2, 3, 1))
print('quadratic(1, 3, -4)=', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 2))


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())


# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# print(calc(1, 2, 3))
# nums = [1, 2, 3]
# print(calc(*nums))


# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# person('Michael', 30)
# person('Michael', 30, city='Beijing', job='Engineer')
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)


# 参数顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


f1(1, 2)
f1(1, 2, 3, 'a', 'b', x=99)


def product(x, *args):
    for i in args:
        x = x * i
    return x


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


# 递归函数（过深调用会导致溢出）
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(100))


# 尾递归优化
def fact_new(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 汉诺塔利用递归实现（圆盘数量、起始柱子、辅助柱子、终点柱子）
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')


# def move(n, a, b, c):
#     global step
#     if n == 1:
#         step = step + 1
#         print(step, '.', a, '-->', c)
#     else:
#         move(n - 1, a, c, b)
#         move(1, a, b, c)
#         move(n - 1, b, a, c)
#
#
# def main():
#     move(3, 'A', 'B', 'C')
#
#
# if __name__ == '__main__':
#     global step
#     step = 0
#     main()

# (0, 1, 2, 3, 4, 5)[:3]
# 'ABCDEFG'[::2]


def trim(s):
    if s == '' or s[0] != ' ' and s[-1] != ' ':
        return s
    elif s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)

# 判断是否可迭代
isinstance('abc', Iterable)

# enumerate函数可以把一个list变成索引-元素对
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        if not isinstance(L, list):
            raise TypeError('bad operand type')
        elif isinstance(L, list):
            min_new = L[0]
            max_new = L[0]
            for value in L:
                if value <= min_new:
                    min_new = value
                elif value >= max_new:
                    max_new = value
            return (min_new, max_new)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

list(range(1, 11))

v = []
for i in range(1, 11):
    v.append(i * i)
print(v)

# 列表生成式
[x * x for x in range(1, 11)]

# 使用两层循环，可以生成全排列
[m + n for m in 'ABC' for n in 'XYZ']

d = {'x': 'A', 'y': 'B', 'z': 'C'}
[k + '=' + v for k, v in d.items()]

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for i in L1:
    if isinstance(i, str):
        L2.append(i.lower())
    else:
        pass

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

L2 = [s.lower() for s in L1 if isinstance(s, str)]
# L2 = [x.lower() if isinstance(x, str) else x for x in L1]

# generator（生成器）
g = (x * x for x in range(10))
g

next(g)

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        t = (b, a + b)
        a = t[0]
        b = t[1]
        n = n + 1
    return 'done'


print(fib(6))


def fib_gen(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        t = (b, a + b)
        a = t[0]
        b = t[1]
        n = n + 1
    return 'done'


g = fib_gen(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def triangles():
    L = [1]
    yield L
    while True:
        L = [1] + [L[i] + L[i+1] for i in range(len(L) - 1)] + [1]
        yield L


n = 0
results = []
for t in triangles():
    results.append(t)
    n += 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
isinstance([], Iterable)
isinstance([], Iterator)
isinstance(iter([]), Iterator)

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        # 获得下一个值
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


f = abs
f(-10)


# def add(a, b, f):
#     return f(a) + f(b)
#
#
# print(add(-5, 6, abs))
#
#
# def f(x):
#     return x * x

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


# 将str转化为int
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#         digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return digits[s]
#     return reduce(fn, map(char2num, s))
#
#
# t = str2int('13579')
# print(t)


def normlize(name):
    return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normlize, L1))
L2


def prod(L):
    def cheng(x, y):
        return x * y
    return reduce(cheng, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# def str2float(s):
#     def last(x, y):
#         return x * 10 + y
#
#     def str2num(s):
#         digits = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return digits[s]
    # s中只保留数字filter(str.isdigit, s)
    # result = reduce(last, (map(str2num, filter(str.isdigit, s))))
    # return result * 0.001


# def str2float(s):
#     """字符串转浮点型"""
#
#     def char2num(c):
#         """字符转数字"""
#
#         digists = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return digists[c]

    # split()通过指定分隔符对字符串进行切片
    # s_split = s.split('.')

    # pro_num = reduce(lambda x, y: x * 10 + y, map(char2num, s_split[0]))  # 获得整数部分
    # 倒序输出[::-1]
    # sub_num = reduce(lambda x, y: x * 0.1 + y, map(char2num, s_split[1][::-1]))
    # sub_num = sub_num * 0.1  # 获得小数部分
    # return pro_num + sub_num


# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')


# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15]))

# 把一个序列中的空字符串删掉


def not_empty(s):
    return s and s.strip()


list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))


# 产生所有素数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    """筛选函数"""
    return lambda x: x % n > 0


def primes():
    yield 2
    """初始序列"""
    it = _odd_iter()
    while True:
        """返回序列的第一个值"""
        n = next(it)
        yield n
        """构造新序列"""
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 100:
        print(n)
    else:
        break


# 回数是指从左向右读和从右向左读都是一样的数

def is_palindrome(n):
    return str(n) == (str(n))[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


sorted([36, 5, -12, 9, -21])

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
sorted([36, 5, -12, 9, -21], key=abs)

# 默认情况下，对字符串排序，是按照ASCII的大小比较的
sorted(['Bob', 'about', 'Zoo', 'Credit'])

# 忽略大小写的排序
sorted(['Bob', 'about', 'Zoo', 'Credit'], key=str.lower)

# 要进行反向排序
sorted(['Bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
# print(L2)


def by_score(t):
    return -t[1]


L2 = sorted(L2, key=by_score)
print(L2)


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


list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
f(5)

L = list(filter(lambda x: x % 2 == 1, range(20)))
L


# def now():
#     print('2019-7-26')
#
#
# f = now
# f()
#
# now.__name__
# f.__name__

# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
def log(text):
    def decorator(func):
        """把原始函数的__name__等属性复制到wrapper()函数中"""
        @ functools.wraps(func)
        def wrapper(*arg, **kw):
            print('%s call %s():' % (text, func.__name__))
            return func(*arg, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2019-7-26')


now()

now.__name__


def metric(fn):
    @ functools.wraps(fn)
    def shijian(*arg, **kw):
        print('%s execute in %s ms' % (fn.__name__, 10.24))
        return fn(*arg, **kw)
    return shijian


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

