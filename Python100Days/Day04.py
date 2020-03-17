# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/11 19:38
desc: 循环结构
"""

import random


# 猜字谜游戏
answer = random.randint(0, 100)  # 生成[0, 100]中的一个随机数，而np.random.randint(0, 100)生成范围为[0,100)
count = 0
while True:
    count += 1
    number = int(input("请输入你猜的数字："))
    if number < answer:
        print("数字需要大一点！\n")
    elif number > answer:
        print("数字需要小一点！\n")
    else:
        print("恭喜你，猜对啦！你总共使用了{}次".format(count))
        break
if count >= 5:
    print("居然用了这么多次，你的智商欠费啦！\n")


# 画左下三角
row = int(input("\n请输入行数："))
for i in range(row):
    for _ in range(0, i + 1):
        print("*", end = " ")
    print()  # 换行，print默认是打印一行，结尾加换行
print("--------------------------")
# 画右下三角
for i in range(row):
    for j in range(row):
        if j < (row - i - 1):
            print(" ", end = " ")
        else:
            print("*", end = " ")
    print()  # 换行，print默认是打印一行，结尾加换行
print("--------------------------")
# 画正三角
for i in range(row):
    for _ in range(row - i - 1):
        print(" ", end = " ")
    for _ in range(2 * i + 1):
        print("*", end = " ")
    print()  # 换行，print默认是打印一行，结尾加换行


# 求解最大公因数和最小公倍数
num = int(input("\n请输入第一个整数num："))
den = int(input("请输入第二个整数den："))
if num > den:
    num, den = den, num
for i in range(num, 0, -1):
    if num % i == 0 and den % i == 0:
        print("{}和{}的最大公因数为：{}, 最小公倍数为：{}".format(num, den, i, num * den // i))
        break


