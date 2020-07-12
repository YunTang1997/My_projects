# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/7/11
desc: 0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
"""


# 方法一（超出时间限制）
def lastRemaining1(n, m):
    nList = [i for i in range(n)]
    i = 0
    for _ in range(n - 1):  # 每循环一次删除一个数
        count = 0  # 报数
        while count < m:  # 每数到m将该元素记为False，代表将它从列表剔除
            if nList[i] is not False:
                count += 1
            if count == m:
                nList[i] = False
            i = (i + 1) % n
    for i in range(n):
        if nList[i] is not False:
            return nList[i]


# 方法二
def lastRemaining2(n, m):
    nList = [i for i in range(n)]
    i = 0
    for j in range(n, 1, -1):
        i = (i + m - 1) % j
        nList.pop(i)
    return nList[0]


# 方法三（找递推公式）
def lastRemaining3(n, m):
    pos = 0
    for i in range(2, n + 1):
        pos = (pos + m) % i
    return pos


if __name__ == '__main__':
    print(lastRemaining1(5, 3))
    print(lastRemaining1(10, 17))
    print(lastRemaining1(50, 7))
    print(lastRemaining2(5, 3))
    print(lastRemaining2(10, 17))
    print(lastRemaining2(50, 7))
    print(lastRemaining3(5, 3))
    print(lastRemaining3(10, 17))
    print(lastRemaining3(50, 7))



