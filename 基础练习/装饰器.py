import functools
import time

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
# def log(text):
#     def decorator(func):
#         """把原始函数的__name__等属性复制到wrapper()函数中"""
#         @ functools.wraps(func)
#         def wrapper(*arg, **kw):
#             print('%s call %s():' % (text, func.__name__))
#             return func(*arg, **kw)
#         return wrapper
#     return decorator


# @log('execute')
# def now():
#     print('2019-7-26')


# now()

# now.__name__


# 练习


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


# 小结
# def log(fnc):
#     @functools.wraps(fnc)
#     def wrapper(*arg, **kv):
#         print('begin call')
#         g = fnc(*arg, **kv)
#         print('end call')
#         return g
#     return wrapper
#
#
# @log
# def now():
#     print(2019-7-26)
#
#
# now()


def log(text='run'):
    def decorator(fnc):
        @functools.wraps(fnc)
        def wrapper(*arg, **kv):
            if isinstance(text, str):
                print('%s() %s in %s:' % (fnc.__name__, text, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            else:
                print('%s() %s in %s:' % (fnc.__name__, 'run', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            return fnc(*arg, **kv)
        return wrapper
    """检查是否可调用"""
    if callable(text):
        return decorator(text)
    else:
        return decorator


@log
def now():
    print('Have a good day!')


now()


@log('execute')
def now():
    print('Have a good day!')


now()














