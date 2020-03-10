"""
将华氏温度转化为摄氏温度
输入圆的半径计算圆周长和面积
输入年份 如果是闰年输出True 否则输出False
"""

import math


f = float(input("请输入华氏温度："))
c = (f - 32) / 1.8
# print("%.1f华氏度 = %.1f摄氏度" % (f, c))  # 占位型语法
print("{:.1f}华氏度 = {:.1f}摄氏度".format(f, c))  # 格式化函数

radius = float(input("请输入圆的半径："))
perimeter = math.pi * (2 * radius)
area = math.pi * radius ** 2
# print("圆的周长为：%.2f，圆的面积为：%.2f" % (perimeter, area))
print("圆的周长为：{:.2f}，圆的面积为：{:.2f}".format(perimeter, area))

year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(str(year) + "年是闰年")
else:
    print(str(year) + "年不是闰年")
