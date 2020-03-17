# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/17
desc: 第七天练习代码
"""


import os
import time
import random


# 在屏幕上显示跑马灯文字
def main():
    content = "北京欢迎你为你开天辟地…………"
    while True:
        # 清理屏幕上的输出
        os.system("cls")  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
# def generate_code(num_code_len=2, alp_code_len=2):
#     num = "0123456789"
#     alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     num_part = ""
#     for _ in range(num_code_len):
#         num_index = random.randint(0, len(num)-1)
#         num_part += num[num_index]
#     alp_part = ""
#     for _ in range(alp_code_len):
#         alp_idex = random.randint(0, len(alpha)-1)
#         alp_part += alpha[alp_idex]
#     return num_part + alp_part

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

#  设计一个函数返回给定文件名的后缀名
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.find(".")
    if 0 < pos < len(filename)-1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return "此文件没有后缀名"

# 设计一个函数返回传入的列表中最大和第二大的元素的值
# def max2(list_new):
#     max_list = [0, 0]
#     n = 0
#     go_on = True
#     while go_on:
#         list_index = len(list_new)
#         for i in range(list_index):
#             if max_list[n] >= list_new[i]:
#                 max_list[n] = max_list[n]
#             else:
#                 max_list[n] = list_new[i]
#         list_new.remove(max_list[n])
#         go_on = True if n == 0 else False
#         n += 1
#     return f"该列表第一大元素为：{max_list[0]}，第二大元素为：{max_list[1]}"

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for i in range(2, len(x)):
        if x[i] > m1:
            m2 = m1
            m1 = x[i]
        elif x[i] > m2:
            m2 = x[i]
    return m1, m2

# 计算指定的年月日是这一年的第几天
def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, day):
    """
    计算传入的日期是这一年的第几天
    :param year: 年份
    :param month: 月份
    :param day: 第几天
    :return:
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for i in range(month - 1):
        total += days_of_month[i]
    total += day
    return total

# 打印杨辉三角
def main():
    num = int(input("Number of rows: "))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end="\t")  # end="\t"表示每一次print在末尾加的制表符，而不是换行
        print()  # 换行


if __name__ == '__main__':
#     main()
    print(generate_code())
    print(get_suffix("123456.py", True))
    # print(get_suffix("123456"))
    print(max2([8, 9, 5, 10, -1, 9.5]))
    print(which_day(1980, 11, 28))
    # print(which_day(1981, 12, 31))
    # print(which_day(2018, 1, 1))
    # print(which_day(2016, 3, 1))
    main()