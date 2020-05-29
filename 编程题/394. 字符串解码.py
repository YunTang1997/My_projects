# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/28
desc: 字符串解码
"""


import re


# 方法一
def decodeString_1(s):
    stack = []   # (str, int) 记录之前的字符串和括号外的上一个数字
    num, res = 0, ''
    for chr in s:
        if chr.isdigit():  # isdigit()判断字符串是否全是由数字组成
            num = num * 10 + int(chr)
        elif chr == '[':
            stack.append((res, num))
            num, res = 0, ''
        elif chr == ']':
            top = stack.pop()
            res = top[0] + res * top[1]
        else:
            res += chr
    return res


# 方法二
def decodeString_2(s):
    stack1 = []  # 储存数字字符和-1，每次遇到'['，就向stack1中存入-1用于给数字字符分层
    stack2 = []  # 储存'['和字母字符，其中'['用于分层
    for chr in s:
        if chr in '0123456789':  # 遇到数字字符压入stack1
            stack1.append(chr)
        elif chr == '[':  # 遇到'['，向stack1中压入-1， 向stack2中压入'['
            stack1.append(-1)
            stack2.append(chr)
        elif chr == ']':  # 遇到']'则将该层的字符转化为正确的字符，并将结果压入stack2
            tmp_char_list = []  # 用于临时储存本层的字母字符
            while stack2 and stack2[-1] != '[':
                tmp_char_list.append(stack2.pop())
            stack2.pop()  # 弹出本层分界字符'['
            tmp_char_list = ''.join(tmp_char_list[::-1])  # 将本层字母字符按正确的顺序拼接起来，注意要采用逆序输出，因为前面压入采用的append方法
            tmp_num =''  # 用于临时储存本层的数字字符
            stack1.pop()  # 弹出用于分界的数字-1
            while stack1 and stack1[-1] != -1:
                tmp_num += stack1.pop()
            tmp_num = int(tmp_num[::-1])  # 将本层数字字符按正确的顺序拼接起来并转化为整数，注意要采用逆序输出，因为前面压入采用的append方法
            stack2.append(tmp_char_list * tmp_num)  # 将该层解码后的字符串压入stack2
        else:  # 字母字符全部压入stack2
            stack2.append(chr)
    return ''.join(stack2)  # 将stack2中的所有字符串拼接，得到答案


# 方法三
def decodeString_3(s):
    regex = re.compile(r'(\d+)\[(\w+)\]')
    match = regex.findall(s)  # 返回一个表，表中元素是按顺序给出的皮匹配得到的各个子串（从左到右，非重叠）
    while match:  # 知道没有匹配到符合的字符串
        for tmp_num, tmp_string in match:
            s = s.replace(tmp_num + '[' + tmp_string + ']', tmp_string * int(tmp_num))  # 由里向外逐步替换为解码后的字符串
        match = regex.findall(s)
    return s



if __name__ == '__main__':
    print(decodeString_1('3[a20[c]]'))
    print(decodeString_2('3[a20[c]]'))
    print(decodeString_3('3[a20[c]]'))

