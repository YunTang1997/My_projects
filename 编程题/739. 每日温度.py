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
        while dim_stack and value > dim_stack[-1][1]:  # 循环直至栈顶value>=当前value
            tmp = dim_stack.pop()  # 弹出栈顶元素
            res[tmp[0]] = index - tmp[0]  # 在res对应位置更新结果
        dim_stack.append((index, value))
    return res


def dailyTemperatures_3(T):
    n, dim_stack = len(T), []
    res = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        while dim_stack and T[i] >= T[dim_stack[-1]]:  # 注意此处第二个条件要取=
            dim_stack.pop()  # 弹出对应值<=当前下标对应值的下标
        if dim_stack: # 如果栈非空，说明T[i]右边第一个比它更大的元素是T[dim_stack[-1]]
            res[i] = dim_stack[-1] - i
        else:  # 如果栈空，说明T[i]右边没有比它更大的元素
            res[i] = 0
        dim_stack.append(i)
    return res


if __name__ == '__main__':
    print(dailyTemperatures_1([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dailyTemperatures_1([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
    print(dailyTemperatures_2([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dailyTemperatures_2([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
    print(dailyTemperatures_3([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dailyTemperatures_3([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
