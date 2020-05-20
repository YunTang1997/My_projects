# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/20
desc: 每个元音包含偶数次的最长子字符串
"""


def findTheLongestSubstring(s):
    """
    定义特征，aeiou分别对应二进制00001，00010，00100，01000，10000
    其中0表示对应元音出现了偶数次数，1表示奇数
    """
    n = len(s)
    bin_reocord = [-float('inf')] * (1 << 5)  # 储存'aeiou'五个元音字符在子串中的奇偶情况，'00000'(0)~'11111'(31)总共32种状态
    bin_reocord[0] = -1  # 处理边界情况，方便计算子串的长度
    res, status = 0, 0
    for i in range(n):
        #  注意异或运算符的应用
        if s[i] == 'a':
            status ^= (1 << 0)
        elif s[i] == 'e':
            status ^= (1 << 1)
        elif s[i] == 'i':
            status ^= (1 << 2)
        elif s[i] == 'o':
            status ^= (1 << 3)
        elif s[i] == 'u':
            status ^= (1 << 4)
        if bin_reocord[status] != -float('inf'):  # 表示子串中各元音字符次数奇偶状态（status）重复出现
            cur_len = i - bin_reocord[status]  # 计算当前满足条件的子串长度
            res = max(res, cur_len)  # 更新符合条件的子串最长长度
        else:  # 表示子串中各元音字符次数奇偶状态（status）首次出现
            bin_reocord[status] = i  # 记录首次出现时对应下标
    return res


if __name__ == '__main__':
    print(findTheLongestSubstring("eleetminicoworoep"))
    print(findTheLongestSubstring("leetcodeisgreat"))
    print(findTheLongestSubstring("bcbcbc"))