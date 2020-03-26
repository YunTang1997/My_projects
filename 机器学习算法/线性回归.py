# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/25 10：08
desc: 线性回归算法
"""


# 在开头加上from __future__ import
# print_function这句之后，即使在python2.X，使用print就得像python3.X那样加括号使用
from __future__ import print_function
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


# 加载txt和csv文件
def loadtxtAndcsv_data(fileName, split, dataType):
    return np.loadtxt(fileName, delimiter=split, dtype=dataType)


# 加载npy文件
def loadnpy_data(fileName):
    return np.load(fileName)


def featureNormaliza(X):
    """
    标准化（也可以用归一化）
    :param X: 真实数据矩阵X加了一列1，因为存在theta(0)
    :return: 归一化之后的X以及每一列的均值和标准差
    """
    X_norm = np.array(X)  # 将X转化为numpy数组对象，才可以进行矩阵的运算
    mu = np.zeros((1, X.shape[1]))  # 给每一组数据的均值分配空间
    sigma = np.zeros((1, X.shape[1]))  # 给每一组数据的sigma分配空间

    mu = np.mean(X_norm, 0)  # 求每一列的平均值（0指定为列，1代表行）
    sigma = np.std(X_norm, 0)  # 求每一列的标准差
    for i in range(X.shape[1]):
        X_norm[:, i] = (X_norm[:, i] - mu[i]) / sigma[i]
    return X_norm, mu, sigma


def computerCost(X, y, theta):
    """
    计算代价函数
    :param X: 真实数据矩阵X加了一列1，因为存在theta(0)
    :param y: 真实数据矩阵y
    :param theta: 参数向量theta
    :return: 距离平方和均值
    """
    m = len(y)
    J = 0

    # J = np.dot((X * theta - y).T, X * theta - y) / (2 * m)
    J = (np.transpose(X * theta - y) * (X * theta - y)) / (2 * m)
    return J


def gradientDescent(X, y, theta, alpha, num_iters):
    """
    梯度下降算法
    :param X: 真实数据矩阵X加了一列1，因为存在theta(0)
    :param y: 真实数据矩阵y
    :param theta:  参数向量theta
    :param alpha: 学习速率
    :param num_iters: 迭代次数
    :return: 所求向量theta，以及所有的代价值
    """
    m = len(y)
    n = len(theta)

    temp = np.matrix(np.zeros((n, num_iters)))  # 暂存每次迭代计算的theta，转化为矩阵形式

    J_history = np.zeros((num_iters, 1))  # 记录每次迭代计算的代价值

    for i in range(num_iters):  # 遍历迭代次数
        h = np.dot(X, theta)  # 计算内积
        temp[:, i] = theta - (alpha / m) * \
            np.dot(np.transpose(X), h - y)  # 计算新的theta值，注意X向量要转置
        theta = temp[:, i]  # 更新theta的值
        J_history[i] = computerCost(X, y, theta)  # 计算代价函数
        # print(".")
    return theta, J_history


# 画二维图，查看标准化情况
def plot_X1_X2(X):
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()


font = FontProperties(
    fname=r"c:\windows\fonts\simsun.ttc",
    size=14)   # 解决windows环境下画图汉字乱码问题

# 画每次迭代代价的变化图
def plotJ(J_history, num_iters):
    x = np.arange(1, num_iters + 1)
    plt.plot(x, J_history)
    plt.xlabel("迭代次数", fontproperties=font)  # 注意指定字体，要不然出现乱码问题
    plt.ylabel("代价值", fontproperties=font)
    plt.title("代价值随迭代次数的变化", fontproperties=font)
    plt.show()


# 测试学习效果（预测）
def predict(mu, sigma, theta):
    result = 0
    value = np.array([1650, 3])
    norm_value = (value - mu) / sigma
    final_value = np.hstack((np.ones((1)), norm_value))

    result = np.dot(final_value, theta)
    return result


def linearRegression(alpha=0.01, num_iters=400):
    print("加载数据...\n")

    data = loadtxtAndcsv_data("data\\data.txt", ",", np.float64)  # 读取数据
    X = data[:, 0:-1]  # X对应0到倒数第2列
    y = data[:, -1]   # y对应最后一列
    m = len(y)  # 总的数据条数
    col = data.shape[1]  # data的列数

    X, mu, sigma = featureNormaliza(X)  # 标准化
    plot_X1_X2(X)   # 画图看一下标准化效果

    X = np.hstack((np.ones((m, 1)), X))  # 在X前加一列1，因为有theta(0)存在

    print("\n执行梯度下降算法....\n")

    theta = np.zeros((col, 1))
    y = y.reshape(-1, 1)  # 将行向量转化为列向量
    theta, J_history = gradientDescent(X, y, theta, alpha, num_iters)

    plotJ(J_history, num_iters)

    predict_value = predict(mu, sigma, theta)

    return mu, sigma, theta, predict_value  # 返回均值mu,标准差sigma,学习的结果theta,预测结果predict_value


# 测试linearRegression函数
def testLinearRegression():
    mu, sigma, theta, predict_value = linearRegression(alpha=0.01, num_iters=400)
    print("X各列均值为：{}".format(mu))
    print("\nX各列标准差为：{}".format(sigma))
    print("\n参数theta向量为：{}".format(theta))
    print("\n参数为[1650, 3]时预测值为：{}".format(predict_value))


if __name__ == '__main__':
    testLinearRegression()