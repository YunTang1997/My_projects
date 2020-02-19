import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# inputfile  = 'C:/Users/tangyun/Desktop/data1.csv'
# data = pd.read_csv(inputfile)
# data = data.iloc[:, 1:5]
#
# speed = data.iloc[:, 0]
# x = data.iloc[:, 1]
# y = data.iloc[:, 2]
# z = data.iloc[:, 3]
#
# x_new = []
# y_new = []
# z_new = []
#
#
# for i in range(len(speed)):
#     if speed[i] == 0:
#         x_new.append(x[i])
#         y_new.append(y[i])
#         z_new.append(z[i])


# x_mean = np.mean(x_new)
# print('X轴加速度均值：' + str(x_mean))
# x_var = np.var(x_new)
# print('X轴加速度方差：' + str(x_var))
# y_mean = np.mean(y_new)
#
# print('Y轴加速度均值：' + str(y_mean))
# y_var = np.var(y_new)
# print('Y轴加速度方差：' + str(y_var))
# z_mean = np.mean(z_new)
#
# print('Z轴加速度均值：' + str(z_mean))
# z_var = np.var(z_new)
# print('Z轴加速度方差：' + str(z_var))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 200  # 图片像素
plt.rcParams['figure.dpi'] = 200  # 分辨率
#
# plt.hist(x_new, label='X轴加速度', fc='r')
# plt.title('X轴加速度频数直方图')
# plt.xlabel('X轴加速度')
# plt.ylabel('频数')

# plt.hist(y_new, label='Y轴加速度', fc='r')
# plt.title('Y轴加速度频数直方图')
# plt.xlabel('Y轴加速度')
# plt.ylabel('频数')

# plt.hist(z_new, label='Z轴加速度', fc='r')
# plt.title('Z轴加速度频数直方图')
# plt.xlabel('Z轴加速度')
# plt.ylabel('频数')
#
# plt.legend()
# plt.show()


# m = []
# t = 0
#
#
# def daisu(speed, acc):
#     while t <= len(speed)-1:
#         if speed[t] == 0 and speed[t+1] == 0 and acc[t] != 0 and acc[t+1] != 0:
#             t1 = 2
#             while acc[t+t1] == 0 and t + t1 < len(speed):
#                 t1 = t1 + 1
#             t_new = t + t1
#             if speed[t_new] != 0 and speed[t_new+1] != 0:
#                 t2 = 2
#                 while speed[t_new+t2] != 0 and t_new+t2 < len(speed):
#                     t2 = t2 + 1
#                 t_new1 = t_new + t2
#                 m.append([t, t_new1])
#             t = t_new1 + 1
#         else:
#             t = t + 1
#     return m


# def zhibiao(data):
#     pjsudu = sum(data) / (len(data))  # 平均速度
#
#     xs = []  # 行驶状态
#     for i in range(len(data)):
#         if data[i] != 0:
#             xs.append(data[i])
#     pjxsudu = sum(xs) / (len(xs))  # 平均行驶速度
#
#     sustd = np.std(data, ddof=1)  # 速度标准差
#
#     jiasudu = []  # 加速度序列
#     big0 = []  # 加速度大于0.15部分
#     for i in range(len(data)-1):
#         x = (data[i+1] - data[i]) / 3.6
#         jiasudu.append(x)
#
#     for i in range(len(jiasudu)):
#         if jiasudu[i] > 0.15:
#             big0.append(jiasudu[i])
#     pjjiasudu = sum(big0) / len(big0)  # 平均加速度
#     jiasubi = len(big0) / len(data)  # 加速时间比
#
#     small0 = []  # 加速度小于-0.15部分
#     for i in range(len(jiasudu)):
#         if jiasudu[i] < -0.15:
#             small0.append(jiasudu[i])
#     pjjiansudu = sum(small0) / len(small0)  # 平均减速度
#     jiansubi = len(small0) / len(data)  #  减速时间比
#
#     jiasustd = np.std(big0, ddof=1)  # 加速度标准差
#
#     jiansustd = np.std(small0, ddof=1)  # 减速标准差
#
#     daisutime = []
#     for i in range(len(data)):
#         if data[i] == 0:
#             daisutime.append(data[i])
#     daisubi = len(daisutime) / len(data)  # 怠速时间比
#
#     yunsubi = 1 - jiasubi - jiansubi - daisubi  # 匀速时间比
#
#     return [pjsudu, pjxsudu, sustd, pjjiasudu, jiasubi, pjjiansudu, jiansubi, jiasustd, jiansustd,\
#             daisubi, yunsubi]


data = pd.read_csv('C:/Users/tangyun/Desktop/goku3.csv')
# print(zhibiao(data.iloc[:, 1]))

plt.plot(data.iloc[:, 0], 'r')
plt.title('清洗数据后文件3的汽车行驶工况')
plt.xlabel('时间（S）')
plt.ylabel('速度（Km/h）')
plt.show()














