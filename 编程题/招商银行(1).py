# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/13
desc: 招商银行信用卡中心
"""


import sys


def reverse(list):
    i, j = 0, len(list) - 1
    while i < j:
        list[i], list[j] = list[j], list[i]
        i, j = i + 1, j - 1
    return list


def game(number):

    re_number = reverse(number.copy())
    length = len(number)
    test = []

    for i in range(length):
        if number[i] == '1' and re_number[i] == '1':
            test.append(True)
        elif (number[i] == '3' and re_number[i] == '8') or (number[i] == '8' and re_number[i] == '3'):
            test.append(True)
        elif abs(int(number[i]) - int(re_number[i])) == 3:
            test.append(True)
        else:
            test.append(False)

    if test == [True] * length:
        result = 'YES'
    else:
        result = 'NO'
    return result


if __name__ == '__main__':

    # x = ['69', '6996', '1111']
    input_ = sys.stdin.readline().strip().split(" ")

    i = 0
    while i <= 2:
        number = list(input_[i])
        print(game(number))
        i += 1
