# coding = utf-8

"""
Author: YunTang
version: 0.1
date:
desc:
"""


import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler  # 引入缩放的包


data = np.loadtxt("data\\data.txt", delimiter=",", dtype=np.float64)
X = data[:, 0:-1]
y = data[:, -1]



# 标准化
scaler = StandardScaler()
scaler.fit(X)
x_trian = scaler.transform(X)
x_test = scaler.transform(np.array([1650, 3]).reshape(1, -1))
# x_test = scaler.transform(np.asmatrix(np.array([1650, 3])))


# 线性模型拟合
model = linear_model.LinearRegression()
model.fit(x_trian, y)


# 预测
result = model.predict(x_test)
print(result)
