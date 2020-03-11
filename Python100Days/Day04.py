# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/11 19:38
desc: 循环结构
"""

import random


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
        print("恭喜你，猜对啦！你总共使用了{}次\n".format(count))
        break
if count >= 5:
    print("居然用了这么多次，你的智商欠费啦！")
