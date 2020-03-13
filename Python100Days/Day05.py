# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/13
desc: 构造程序逻辑
"""
import random
import math


#  寻找水仙花数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身
shuixh = []
for num1 in range(100, 1000):
    low = num1 % 10
    mid = num1 // 10 % 10
    high = num1 // 100
    if low ** 3 + mid ** 3 + high ** 3 == num1:
        shuixh.append(num1)
print("水仙花数为：{}".format(shuixh))

print("-------------------------------------")
# 正整数反转
num2 = int(input("请输入你想颠倒的数："))
reverse = 0
while num2 > 0:
    reverse = num2 % 10 + reverse * 10
    num2 = num2 // 10
print("颠倒之后的数为：{}".format(reverse))

print("-------------------------------------")
# 百钱百鸡问题（穷举法）
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - y - x
        if 5 * x + 3 * y + z / 3 == 100:
            print("鸡公{}只，鸡母{}只，鸡仔{}只".format(x, y, z))

print("-------------------------------------")
# CRAPS赌博游戏
money = 1000
n = 0  # 记录游戏轮数
while money > 0:
    n += 1  # 游戏轮数+1
    count = 0  # 每一轮新游戏投骰子次数清零
    first = 0  # 每一轮新游戏第一次骰子数清零
    second = 0  # 每一轮新游戏第二次及以后骰子数清零
    print("\n第{}轮游戏，你的总资产为：{}".format(n, money))
    needs_go_on = False
    while True:
        debt = int(input("请下注："))
        if 0 < debt <= money:
            break
    first = random.randint(1, 6) + random.randint(1, 6)
    count += 1  # 投骰子次数+1
    print("第{}轮第{}次的点数为：{}".format(n, count, first))
    if first == 7 or first == 11:
        print("玩家胜！")
        money = money + debt
    elif first == 2 or first == 3 or first == 12:
        print("庄家胜！")
        money = money - debt
    else:
        needs_go_on = True
    while needs_go_on:
        second = random.randint(1, 6) + random.randint(1, 6)
        count += 1  # 投骰子次数+1
        print("第{}轮第{}次的点数为：{}".format(n, count, second))
        if second == 7:
            print("庄家胜！")
            money = money - debt
            needs_go_on = False
        elif second == first:
            print("玩家胜！")
            money = money + debt
            needs_go_on = False
        else:
            pass
print("天台见！")

print("-------------------------------------")
# 斐波那契数列
fib = []
num, den = 0, 0
for i in range(20):
    if i == 0:
        num, den = 0, 1
        fib.append(den)
    else:
        num, den = den, num + den
        fib.append(den)
print("斐波那契数列前20位：{}".format(fib))

print("-------------------------------------")
# 完美数
perfect = []  # 完美数列表
for i in range(1, 10000):
    z = []  # 真因素列表，完成一次大循环后都会清空
    for j in range(1, i):
        if i % j == 0:
            z.append(j)
    if sum(z) == i:
        perfect.append(i)
print("10000以内的完美数为：{}".format(perfect))

print("-------------------------------------")
# 素数
prime = []
for i in range(2, 100):
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
print("100以内的素数为：{}".format(prime))
