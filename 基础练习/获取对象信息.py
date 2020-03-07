import types
# type(123)
# type('str')
# type(None)
#
# type(abs)
#
# type(123) == type(456)
#
# type(123) == int
#
# type('abc') == type(123)


# def fn():
#     pass


# type(fn) == types.FunctionType
# type(abs) == types.BuiltinFunctionType
# type(lambda x: x) == types.LambdaType
# type((x for x in range(10))) == types.GeneratorType

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”
# isinstance('a', str)
# isinstance(123, int)
# isinstance(b'a', bytes)
# isinstance([1, 2, 3], (list, tuple))
# isinstance((1, 2, 3), (list, tuple))

# 获得一个对象的所有属性和方法
# dir('ABC')
#
# len('ABC')
# 'ABC'.__len__()
#
#
# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#
#     def __len__(self):
#         return 100
#
#     def power(self):
#         return self.x * self.x
#
#
# dog = MyObject()
# len(dog)
#
# obj = MyObject()

# 有属性'x'吗
# hasattr(obj, 'x')
#
# obj.x
#
# hasattr(obj, 'y')

# 设置一个属性'y'
# setattr(obj, 'y', 19)
# hasattr(obj, 'y')

# 获取属性'y'
# getattr(obj, 'y')
# obj.y

# 获取对象方法并调用
# fn = getattr(obj, 'power')
# fn
# fn()


