import re


# a = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# b = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
# print(a)

# test = '010-12345'
# if re.match(r'^\d{3}\-\d{3,8}$', test):
#     print('ok')
# else:
#     print('failed')

# 用正则表达式切分字符串比用固定的字符更灵活
# c = re.split(r'\s+', 'a b  c')
# print(c)
# d = re.split(r'[\s\,]+', 'a,b, c  d')
# print(d)
# e = re.split(r'[\s\,\;]+', 'a,b;; c  d')
# print(e)

# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组
# f = re.match(r'^(\d{3})\-(\d{3,8}$)', '010-12345')
# print(f)
# print(f.group(0))  # 匹配到的原始字符串
# print(f.group(1))  # 第一个子串
# print(f.group(2))  # 第二个字串

# t = '19:05:30'
# m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])'
#              r'\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# print(m.groups())


# 贪婪匹配
# g = re.match(r'^(\d+)(0*)$', '102300')  # \d+会将末尾的两个0也匹配掉
# g = re.match(r'^(\d+?)(0*)$', '102300')  # 加个?就可以让\d+采用非贪婪匹配
# print(g.groups())

# 编译
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 将正则表达式编译好，后面直接用
# h = re_telephone.match('010-12345')
# print(h.groups())


# 练习
# def is_valid_email(addr):
#     if re.match(r'^[\w.]+@\w+\.\w{3}$', addr):
#         return True
#     else:
#         return False
#
#
# assert is_valid_email('someone@gmail.com')  # assert断言函数，条件为真继续执行，条件为假则报错
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')
#
# print('----------------------------------------')


# def name_of_email(addr):
#     if re.match(r'^\<([\w\s]+)\>\s?\w*|(\w+)\@[\w\.]+$', addr):
#         a = list(re.match(r'^\<([\w\s]+)\>\s?\w*|(\w+)\@[\w\.]+$', addr).groups())
#         for i in range(len(a)):
#             if a[i] is None:
#                 del(a[i])
#             return a[0]
#     else:
#         return None
#
#
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
# print('ok')


# def name_of_email(addr):
#     f = re.match(r'^<?([\w\s]+)>?\s?\w*@[\w.]+$', addr)
#     if f:
#         return f.group(1)
#     else:
#         return None
#
#
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
# print('ok')


def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

