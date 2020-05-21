# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 字符串转换为整数
desc: 2020/5/21
"""


import  re


def myAtoi(str):
    str = str.lstrip(" ")  # 去掉字符串左边的空格字符
    regex = re.compile("[+-]?\d+")  # 生成需要的正则表达式对象
    if regex.match(str):  # 匹配成功
        res = int(regex.match(str).group())  # 匹配符合正则表达式对象的目标串前缀
    else:   # 否则匹配失败
        return 0  # 返回0

    # if res > pow(2, 31) - 1:
    #     return pow(2, 31) - 1
    # elif res < -pow(2, 31):
    #     return -pow(2, 31)
    # else:
    #     return res

    return max(min(res, (1 << 31) - 1), -(1 << 31))


if __name__ == '__main__':
    print(myAtoi(""))
    print(myAtoi(" "))
    print(myAtoi("+"))
    print(myAtoi("-"))
    print(myAtoi("+++++"))
    print(myAtoi("---++"))
    print(myAtoi("+-+-"))
    print(myAtoi("42"))
    print(myAtoi("   -42"))
    print(myAtoi("4193 with words"))
    print(myAtoi("words and 987"))
    print(myAtoi("-91283472332"))


