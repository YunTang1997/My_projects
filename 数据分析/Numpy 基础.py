from timeit import default_timer as timer  # 计算代码运行时间模块
from numpy.linalg import inv, qr  # 求矩阵的逆和QR分解
import random
import numpy as np
import matplotlib.pyplot as plt


# my_arr = np.arange(1000000)
# my_list = list(range(1000000))

# start1 = timer()
# my_arr2 = my_arr * 2
# end1 = timer()
# print(end1 - start1)  # 输出时间单位为s
# print('\n')

# start2 = timer()
# my_list2 = [x * 2 for x in my_list]
# end2 = timer()
# print(end2 - start2)

# print('\n-----NumPy ndarry：多维数组对象------')
# data = np.random.randn(2, 3)
# print(data)
# print('\n')
# print(data * 10)
# print('\n')
# print(data + data)
# print('\n')
# print(data.shape)  # shape属性，用来表征数组每一维度的数量
# print(data.dtype)  # dtype属性，用来描述数组的数据类型

# print(np.zeros(10))
# print(np.zeros((3, 6)))
# print(np.empty((2, 3, 2)))

# arr1 = np.array([1, 2, 3], dtype=np.float64)  # 生成指定数据类型的数组
# arr2 = np.array([1, 2, 3], dtype=np.int32)

# arr = np.array([1, 2, 3, 4, 5])
# float_arr = arr.astype(np.float64)  # 利用astype方法将转换数组的数据类型

# numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
# print(numeric_strings)
# print(numeric_strings.astype(np.float64))  # 将字符串转化为数字

# int_array = np.arange(10)
# calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
# print(int_array.astype(calibers.dtype))  # 使用另外一个数组的dtype属性

# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2d)
# print(arr2d[:2])  # 读取前2行
# print(arr2d[:2, 1:])  # 读取前两行的后两列
# print(arr2d[1, :2])  # 读取第二行的前两列
# print(arr2d[:2, 2])  # 读取前两行的第三列
# print(arr2d[:, :1])  # 读取第一列，此处得到的仍然是二维的
# print(arr2d[:, 0])  # 读取第一列，但是索引和切片组合会得到低维毒的切片，例如此处得到的是一维的

# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# data = np.random.randn(7, 4)
# print(data)
# print(data[names == 'Bob'])  # 选中所有'Bob'对应的行
# print('\n')
# print(data[names == 'Bob', 3:])
# print('\n')
# print(data[names == 'Bob', 3])

# print(data[~(names == 'Bob')])  # ~取反
# print(data[names != 'Bob'])

# print((names == 'Bob') & (names == 'Will'))  # 对布尔值数组，and和or是没有用的，只有&和|是有用的

# arr = np.empty((8, 4))
# for i in range(8):
#     arr[i] = i
# print(arr)
# print(arr[[4, 3, 0, 6]])
# print(arr[[-3, -5, -7]])

# arr = np.arange(32).reshape((8, 4))
# print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])  # 元素（1， 0）、（5， 3）、（7， 1）和（2， 2）会被选中

# arr = np.arange(32).reshape((8, 4))
# # print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])  # 元素（1， 0）、（5， 3）、（7， 1）和（2， 2）会被选中
# # print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])  # 得到矩行中行列的子集所形成的矩性区域

# arr = np.arange(15).reshape((3, 5))
# print(arr.T)  # T属性转置
# print(np.dot(arr.T, arr))  # 计算矩阵内积

# arr = np.arange(16).reshape((2, 2, 4))
# # print(arr)
# print(arr.transpose((1, 0, 2)))
# print('\n')
# print(arr.swapaxes(1, 2))
# print('\n')
# print(arr.swapaxes(2, 1))

print('\n-----通用函数：快速的逐元素数组函数------')
# arr = np.arange(10)
# print(np.sqrt(arr))
# print('\n')
# print(np.exp(arr))
# print('\n')

# x = np.random.randn(8)
# y = np.random.randn(8)
# print(np.maximum(x, y))

# arr = np.random.randn(7) * 5
# remainder, whole_part = np.modf(arr)
# print(remainder)  # 浮点数值小数部分
# print(whole_part)  # 浮点数值整数部分

# arr = np.arange(8).reshape(2, 4)
# print(np.multiply(arr, arr))

'''使用数组进行面向数组编程'''
# points = np.arange(-5, 5, 0.01)
# xs, ys = np.meshgrid(points, points)
# z = np.sqrt(xs ** 2 + ys ** 2)
# plt.imshow(z, cmap=plt.cm.gray)
# plt.colorbar()
# plt.title('Image of plot of $\sqrt{x^2+y^2}$ for a grid of values')
# plt.show()

# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
# cond = np.array([True, False, True, True, False])

# result = [(x if c else y)
#           for x, y, c in zip(xarr, yarr, cond)]
# print(result)
# result_new = np.where(cond, xarr, yarr)  # 更加简单地实现了上述代码
# print(result_new)

# arr = np.random.randn(4, 4)
# result1 = np.where(arr>0, 2, -2)  # 将正值替换为2，将负值替换为-2
# print(result1)
# result2 = np.where(arr>0, 2, arr)  # 将正值替换为2，其余不变
# print(result2)

# arr = np.random.randn(5, 4)
# print(np.sum(arr, axis=0))
# print(np.sum(arr, axis=1))

# arr = np.random.randn(100)
# print((arr > 0).sum())  # 正值的个数

# bools = np.array([False, False, True, True])
# print(bools.any())  # 检查数组中是否至少有一个True
# print(bools.all())  # 检查是否每个值都是True

# arr = np.random.randn(6)
# arr.sort()
# print(arr)
# print(np.sort(arr))

# large_arr = np.random.randn(1000)
# large_arr_new = np.sort(large_arr)
# result = large_arr_new[int(0.05 * len(large_arr_new))]  # 5%分位数
# print(result)

# names = np.array(['BOb', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# print(np.unique(names))  # 返回数组的唯一值并排序
# ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
# print(np.unique(ints))

# values = np.array([6, 0, 0, 3, 2, 5, 6])
# print(np.in1d(values, [2, 3, 6]))  # 检查一个数组中的值是否在另外一个数组中，返回一个布尔值

'''线性代数'''
# x = np.array([[1, 2, 3], [4, 5, 6]])
# y = np.array([[4, 5, 6], [1, 2, 3]])
# print(x * y)  # 注意*是矩阵的逐元素乘积


# x = np.array([[1, 2, 3], [4, 5, 6]])
# y = np.array([[6, 23], [-1, 7], [8, 9]])

# result = np.dot(x, y)  # 矩阵之间的乘积
# print(result)

# print(x @ y)  # 同上矩阵之间的乘积

# X = np.random.randn(5, 5)
# mat = X.T @ X
# print(inv(mat))  # 求解矩阵的逆
# print(mat @ inv(mat))

'''随机漫步'''
# position = 0
# walk = [position]
# steps = 1000
# for i in range(steps):
#     step = 1 if np.random.randint(0, 2) else -1
#     position += step
#     walk.append(position)
# print(walk)
# plt.plot(walk[:100])
# plt.show()

# nsteps = 1000
# draws = np.random.randint(0, 2, size=nsteps)
# steps = np.where(draws > 0, 1, -1)
# walks = steps.cumsum()
# print((np.abs(walks) >= 10).argmax())  # 第一次连续某一方向走了10步的位置

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws, 1, -1)
walks = steps.cumsum(axis=1)
hists = (np.abs(walks) >= 30).any(axis=1)
crossing_times = (np.abs(walks[hists] >= 30)).argmax(axis=1)
