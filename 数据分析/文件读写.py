import numpy as np
import pandas as pd
from openpyxl import Workbook

# 读取文件
# with open('C:/Users/tangyun/Desktop/test.txt', 'r', encoding='UTF-8', errors='ignore') as f:
#     print(f.read())

# 写文件
# with open('C:/Users/tangyun/Desktop/test.txt', 'w') as f:
#     f.write('Hello, word!')

# 在写好得文件后面追加内容
# with open('C:/Users/tangyun/Desktop/test.txt', 'a') as f:
#     f.write('Tony')

# with open('C:/Users/tangyun/Desktop/2019研究生数学数学建模竞赛名单.csv', 'r', encoding='UTF-8', errors='ignore') as f:
#     lines = f.readlines()  # lines()是一个list
#     for line in lines:
#         print(line.strip())  # 把末尾的'\n'去掉


# filename = '2019研究生数学数学建模竞赛名单.csv'
# filepath = os.path.join(os.getcwd(), filename)
# print(filepath)

# a = pd.read_excel('C:/Users/tangyun/Desktop/data.xlsx')
# print(a)
# a = a.iloc[:, 1:]  # 删除第一列
# print(a)
#  读取文档前五行和前两列
# print(a.iloc[0:6, 0:3])
# print(a.loc[0:5, '学号':'性别'])


"""loc-通过行标签索引行数据
    iloc-通过行号（index，从0开始）索引行数据
    ix-通过行标签或者行号索引行数据（基于loc和iloc的混合）
    同理，索引列数据也是如此"""

# data = [[1, 2, 3], [4, 5, 6]]
# index = ['a', 'b']  # 行号
# columns = ['c', 'd', 'e']  # 列号
# df = pd.DataFrame(data, index=index, columns=columns)  # 生成一个数据框
# print(df)
# print(df.loc['a'])  # 读取数据的第一行
# print(df.iloc[0])  # 读取数据的第一行
# print(df.loc[:, 'c'])  # 读取数据的第一列
# print(df.iloc[:, 0])  # 读取数据的第一列
# print(df.loc['a', 'c':'d'])  # 读取数据第一行前两列
# print(df.loc['a', ['c', 'd']])
# print(df.iloc[0, 0:2])  # 读取数据第一行前两列
# print(df.iloc[0, [0, 1]])

# df = pd.DataFrame({'total_bill': [16.99, 10.34, 23.68, 23.68, 54.59],
#                    'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
#                    'sex': ['Female', 'Male', 'Male', 'Male', 'Female']})
# # df.rename(columns={'total_bill': 'A', 'tip': 'B', 'sex': 'C'})  # 数据框更改列名
# df.columns = []
# print(df)
# print(df.dtypes)  # 数据的列名
# print(df.columns)  # 数据列的index
# print(df.index)  # 数据行的index
# print(df.values)  # 数据的值
# print(df.loc[1:3, ['total_bill', 'tip']])
# print(df.iloc[1:4, 0:2])

#  Excel的写入
wb = Workbook()
ws = wb.create_sheet('test')

label = [[0],
         [1],
         [2],
         [3]]
feature = [[0.1, 0.2, 0.3, 0.4, 0.5],
           [0.11, 0.21, 0.31, 0.41, 0.51],
           [0.6, 0.7, 0.8, 0.9, 1.00],
           [1.1, 1.2, 1.3, 1.4, 1.5]]

label = np.array(label)
feature = np.array(feature)

label_input = []
for i in range(len(label)):
    label_input.append(label[i][0])
ws.append(label_input)

# 按行填充
for j in range(len(feature[:, 0])):
    ws.append(feature[j, :].tolist())

# 按列填充
# for j in range(len(feature[0])):
#     ws.append(feature[:, j].tolist())

wb.save('C:/Users/tangyun/Desktop/test.xlsx')