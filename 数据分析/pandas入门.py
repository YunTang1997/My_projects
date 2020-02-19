import pandas as pd
import numpy as np
from pandas import Series, DataFrame


'''pandas数据结构'''
# obj = pd.Series([4, 7, -5, 3])
# print(obj.values)
# print(obj.index)

# obj2 = pd.Series([6, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# print(obj2['a'])
# print(obj2['d'])
# print(obj2[['c', 'a', 'd']])

# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# obj3 = pd.Series(sdata)  # 由已知的字典生成一个Series
# print(obj3)

# states = ['California', 'Ohio', 'Oregon', 'Texas']
# obj4 = pd.Series(sdata, index=states)
# print(obj4)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# frame = pd.DataFrame(data)
# print(frame)
# print(frame.head())  # 取数据框线5行

# frame_new = pd.DataFrame(data, columns=['year', 'state', 'pop'])
# print(frame_new)

# pop = {'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6},
#        'Nevada': {2001: 2.4, 2002: 2.9}}
# frame3 = pd.DataFrame(data=pop)
# print(frame3 )

# pdata = {'Ohio': frame3[:-1]['Ohio'],
#          'Nevada': frame3[:2]['Nevada']}
# print(pd.DataFrame(pdata))


'''基本功能'''
# obj = pd.Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])
# print(obj)

# obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
# print(obj2)

# obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# print(obj3.reindex(np.arange(6), method='ffill'))

# frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
#                      index=['a', 'c', 'd'],
#                      columns=['Ohio', 'Texas', 'California'])
# print(frame)
# print('\n')

# frame2 = frame.reindex(['a', 'b', 'c', 'd'])
# print(frame2)
# print('\n')

# states = ['Texas', 'Utah', 'California']
# print(frame.reindex(columns=states))

# print(frame.loc[['a', 'b', 'c', 'd'], states])


# data = pd.DataFrame(np.arange(16).reshape((4, 4)),
#                     index = ['Ohio', 'Colorado', 'Utah', 'New York'],
#                     columns= ['one', 'two', 'three', 'four'] )
# print(data.iloc[:, :3][data.three>5])


# ser = pd.Series(np.arange(3.))
# print(ser)
# print('\n')
# print(ser.loc[:1])
# print('\n')
# print(ser.iloc[:1])


# df1 = pd.DataFrame(np.arange(12).reshape((3, 4)),
#                    columns=list('abcd'))
# df2 = pd.DataFrame(np.arange(20).reshape((4, 5)),
#                    columns=list('abcde'))

# print(df1)
# print('\n')
# print(df2)
# print(df1+df2)
# print('\n')
# print(df1.add(df2, fill_value=0))
# print('\n')
# print(df1.reindex(columns=df2.columns, fill_value=0))


# frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
#                      columns=list('bde'),
#                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])

# series = frame.iloc[0]
#
# print(frame-series)
#
# series2 = pd.Series(np.arange(3), index=list('bef'))
# print(frame+series2)
#
# series3 = frame.loc[:, 'd']
# print(frame.sub(series3, axis='index'))


'''函数应用和映射'''
# frame = pd.DataFrame(np.random.randn(4, 3),
#                      columns=list('bde'),
#                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])

# f = lambda x: x.max() - x.min()
# print(frame.apply(f))

# def f(x):
#     return pd.Series([x.min(), x.max()], index=['min', 'max'])
# print(frame.apply(f, axis='index'))


'''唯一值、计数和成员属性'''
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'c', 'c'])
uniques = obj.unique()
print(uniques)
print('\n')
print(obj.value_counts())
print('\n')
print(pd.value_counts(obj.values, sort=False))
