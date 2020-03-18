# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/18
desc: 第七天综合案例，双色球选号、约瑟夫环问题、井字棋游戏
"""


import os
from random import randrange, randint, sample


# 双色球选号
def display(balls):
    """
    :param balls:
    :return: 输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=" ")  # 在倒数两个数之间擦一个"|"
        print("{:02}".format(ball), end=" ")
    print()

def random_select():
    """
    :return: 随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []  # 选完一轮号码，将    selected_balls = []  # 选完一轮号码，将selected_balls清空
    # 使用random模块的sample函数来实现从列表中选择不重复的n个元素
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls

def main1():
    n = int(input("机选几注："))
    for _ in range(n):
        display(random_select())

# 约瑟夫环问题
def main2(total, number, non_number):
    """
    约瑟夫环问题
    :param total: 总人数
    :param number: 数到几就会被杀
    :param non_number: 非基督教人数
    :return: 若杀死的全是非基督教人员，返回初始站位
    """
    people = [True] * total
    # num记录数数，每杀死一名非基督教徒，就清零，index记录索引每逢30清零，count剔除的非基督教人数
    num, index, count = 0, 0, 0
    while count < non_number:
        if people[index]:
            num +=1  # 数数加1
            if num == number:
                people[index] = False
                count += 1  # 记录死亡人数
                num = 0  # 数数清零
        index += 1
        index %= 30
    for i in range(len(people)):
        print("{}:基督教徒".format(i + 1), end=" ") if people[i] else print("{}:非基督教徒".format(i + 1), end=" ")

# 井字棋游戏
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main3():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()  # 得到一份init_board的样本
        begin = False
        turn = "X"
        counter = 0
        os.system("cls")  # 清屏，windows不能用os.system("clean")
        print_board(curr_board)
        while counter < 9:
            move = input("轮到{}走棋，请输入位置：".format(turn))
            if curr_board[move] == " ":
                counter += 1
                curr_board[move] = turn
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"
            # os.system("cls")
            print_board(curr_board)
        choice = input("再玩一局？(yes|no)")
        begin = choice == "yes"



if __name__ == '__main__':
    # main1()
    main2(total=30, number=9, non_number=15)
    main3()
