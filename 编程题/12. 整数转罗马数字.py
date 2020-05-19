# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/49
desc: 整数转罗马数字
"""


# 方法一：
def intToRoman_1(num):
    res = ""
    while num > 0:
        if num >= 1000:
            cur = num // 1000
            res = res + 'M' * cur
            num = num % 1000

        elif num >= 900:
            res = res + 'CM'
            num = num % 900

        elif num >= 500:
            res = res + 'D'
            num = num % 500

        elif num >= 400:
            res = res + 'CD'
            num = num % 400

        elif num >= 100:
            cur = num // 100
            res = res + 'C' * cur
            num = num % 100

        elif num >= 90:
            res = res + 'XC'
            num = num % 90

        elif num >= 50:
            res = res + 'L'
            num = num % 50

        elif num >= 40:
            res = res + 'XL'
            num = num % 40

        elif num >= 10:
            cur = num // 10
            res = res + 'X' * cur
            num = num % 10

        elif num == 9:
            res = res + 'IX'
            num = num % 9

        elif num >= 5:
            res = res + 'V'
            num = num % 5

        elif num == 4:
            res = res + 'IV'
            num = num % 4

        else:
            res = res + 'I' * num
            num = 0

    return res


# 方法二：贪婪法
def intToRoman_2(num):
    """
    把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中
    并且按照阿拉伯数字的大小降序排列，这是贪心选择思想
    """
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    n, i= len(nums), 0
    while i < n:
        # 注意：这里是大于等于号，表示尽量使用大的"面值"
        while num >= nums[i]:
            res += romans[i]
            num -= nums[i]
        i += 1
    return res


def intToRoman_3(num):
    romans_nums = (
            ('M', 1000),
            ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
            ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
            ('IX', 9), ('V', 5), ('IV', 4), ('I', 1),
    )
    res = []
    for romans, nums in romans_nums:
        if num >= nums:
            res.extend([romans] * (num // nums))  # extend()将一个列表中每个元素分别添加到另一个列表中，只接受一个参数
            num %= nums
    return "".join(res)


if __name__ == '__main__':
    print(intToRoman_1(58))
    print(intToRoman_1(1994))
    print(intToRoman_1(3994))
    print(intToRoman_2(58))
    print(intToRoman_2(1994))
    print(intToRoman_2(3994))
    print(intToRoman_3(58))
    print(intToRoman_3(1994))
    print(intToRoman_3(3994))






