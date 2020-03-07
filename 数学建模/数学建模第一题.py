import pandas as pd
import re


def tran(x):
    time_new = []
    for i in x:
        datax = re.findall(r'(\d*)\/\d*\/\d*', i, re.S)
        time_new.append(int(datax[0]))

        datay = re.findall(r'\d\/(\d*)\/\d*', i, re.S)
        time_new.append(int(datay[0]))

        dataz = re.findall(r'\d*\/\d*\/(\d*) ', i, re.S)
        time_new.append(int(dataz[0]))

        datax = re.findall(r' (\d*)\:\d*\:\d*', i, re.S)
        time_new.append(int(datax[0]))

        datay = re.findall(r'\d\:(\d*)\:\d*', i, re.S)
        time_new.append(int(datay[0]))

        dataz = re.findall(r'\d*\:\d*\:(\d*)\.', i, re.S)
        time_new.append(int(dataz[0]))
    second = (time_new[6]-time_new[0]) * 365 * 24 * 3600 + (time_new[7]-time_new[1]) * 30 * 24 * 3600 +\
             (time_new[8]-time_new[2]) * 24 * 3600 + (time_new[9]-time_new[3]) * 3600 + (time_new[10]-time_new[4]) * 60\
             + (time_new[11]-time_new[5])
    return second


def data_pre(file):
    n = []  # 记录缺失数据行索引值
    m = []  # 记录时间不连续行索引值
    l = []  # 记录急加速行索引值
    k = []  # 记录急减速行索引值
    j = []  # 记录长时间停车行索引值
    d = []  # 记录怠速情况索引值
    data = pd.read_csv(file)
    time = data.iloc[:, 0]
    for i in range(len(time)):
        if time[i] is None:
            n.append(i)
    for i in range(len(time)-1):
        if 2 <= tran([time[i], time[i+1]]) <= 600 or tran([time[i], time[i+1]]) == 0:
            m.append(i)

    speed = data.iloc[:, 1]
    for i in range(len(time) - 7):
        if (((speed[i+7] - speed[i]) / 3.6) / tran([time[i], time[i+7]])) > 3.97 and tran([time[i], time[i+7]]) == 7:
            l.append([i, i+7])
    for i in range(len(time) - 2):
        if (((speed[i+2] - speed[i]) / 3.6) / tran([time[i], time[i+2]])) < -8 and tran([time[i], time[i+2]]) == 2:
            k.append([i, i+2])

    lon = data.iloc[:, 5]  # 精度
    lat = data.iloc[:, 6]  # 纬度
    location = []
    for i in range(len(lon)):
        location.append([lat[i], lon[i]])

    acc = data.iloc[:, 12]

    r = []
    t = 0
    while t <= len(location)-2:
        if location[t] == location[t+1] and tran([time[t], time[t+1]]) == 1 and acc[t] != 0 and acc[t+1] != 0:
            m1 = 1
            while location[t] == location[t+m1] and tran([time[t], time[t+m1]]) == m1 and acc[t] != 0 and \
                    acc[t+m1] != 0 and t+m1 <= len(location)-2:
                m1 = m1 + 1
            t_new = t + m1
            r.append([t, t_new-1])
            t = t_new
        else:
            t = t + 1

    for i in range(len(r)):
        if tran([time[r[i][0]], time[r[i][1]]]) >= 120:
            j.append(r[i])

    # r1 = []
    t1 = 0
    while t1 <= len(speed)-2:
        m2 = 1
        while tran([time[t1], time[t1+m2]]) == m2 and speed[t1] < 10 and speed[t1+m2] < 10 and t1+m2 <= len(speed)-2:
            m2 = m2 + 1
        t_new1 = t1 + m2
        if tran([time[t1], time[t_new1-1]]) > 180:
            d.append([t1, t_new1-1])
        t1 = t_new1
    # for i in range(len(r1)):
    #     speed_new = speed[r1[i][0]:r1[i][1]]
    #     if set([i < 10 for i in speed_new]) == {True}:
    #         d.append(r1[i])
    return n, m, l, k, j, d


miss = data_pre('C:/Users/tangyun/Desktop/data1.csv')
print(miss[0])  # 记录缺失数据行索引值
print(miss[1])  # 记录时间不连续行索引值
# print(miss[2])  # 记录急加速行索引值
# print(miss[3])  # 记录急减速行索引值
# print(miss[4])  # 记录长时间停车行索引值
# print(miss[5])  # 记录怠速行索引值




