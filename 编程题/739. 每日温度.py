# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/11
desc: 每日温度
"""


# 方法一（暴力法，超出时间限制）
def dailyTemperatures_1(T):
    res = []
    n = len(T)
    for i in range(n - 1):
        count = 0  # 0代表不存在温度上升，1代表存在
        for j in range(i + 1, n):
            if T[j] > T[i]:  # 存在温度上升的情况
                res.append(j - i)  # 需要等待的天数
                count += 1
                break  # 打断内层循环
        if count == 0:  # 不存在温度上升的情况
            res.append(0)
    res.append(0)  # T结尾元素，不存在温度上升的情况，直接加0
    return res


# 方法二（递减栈）
def dailyTemperatures_2(T):
    n, dim_stack = len(T), []
    res = [0 for _ in range(n)]  # 初始化结果全部为0
    for index, value in enumerate(T):
        if not dim_stack:  # 将（0，T[0]）压入栈
            dim_stack.append((index, value))
            continue
        elif value > dim_stack[-1][1]:  # 若当前value>栈顶value
            while dim_stack and value > dim_stack[-1][1]:  # 循环直至栈顶value>=当前value
                tmp = dim_stack.pop()  # 弹出栈顶元素
                res[tmp[0]] = index - tmp[0]  # 在res对应位置更新结果
            dim_stack.append((index, value))  # 跳出while循环并将当前（index，value）压入栈
        else:  # 若当前value<=栈顶value
            dim_stack.append((index, value))
    return res


if __name__ == '__main__':
    print(dailyTemperatures_1([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dailyTemperatures_1([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
    print(dailyTemperatures_2([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dailyTemperatures_2([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
