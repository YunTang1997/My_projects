import pandas as pd
import numpy as np


ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)  # 将年龄分为18~25、26~35、36~60、61~四组
print(cats, "\n")
print("cats的类型:\n", type(cats))
print("年龄的四个区间:\n", cats.categories)
print("各区间含有的样本数:\n", pd.value_counts(cats))

print("-------------------------")
# 传递right=False代表年龄区间左闭右开，默认为True
cats1 = pd.cut(ages, [18, 26, 36, 61, 100], right=False)
print(cats1)

print("-------------------------")
group_names = ["Youth", "YoungAdult", "MiddleAged", "Senior"]
cats2 = pd.cut(ages, bins, labels=group_names)  # 利用labels参数定义各分区的名称
print(cats2)

print("-------------------------")
data = np.random.rand(20)  # 均匀分布
# 利用整数代替分区的具体细节，会自动根据最大值、最小值分成等距的箱，precision=2将十进制精度限制在两位
cats3 = pd.cut(data, 4, precision=2)
print(cats3)

print("-------------------------")
# qcut()基于样本分位数进行分箱，若只给定分箱树，则每个箱具有相同数据量的数据点
data1 = np.random.randn(1000)  # 正态分布
cats4 = pd.qcut(data1, 4)
print(cats4, "\n")
print(pd.value_counts(cats4))

print("-------------------------")
# 也可以传入自定义的分位数（0和1之间）
cats5 = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1])
print(cats5, "\n")
print(pd.value_counts(cats5))