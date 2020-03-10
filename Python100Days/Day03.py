"""
英制单位英寸和公制单位厘米互换
百分制成绩转换为等级制成绩
输入三条边长，如果能构成三角形就计算周长和面积

version: 0.1
Author: YunTang
"""


value = float(input("请输入长度："))
unit = input("请输入单位：")
if unit == "in" or unit == "英寸":
    print("{:.1f}英寸为{:.1f}厘米\n".format(value, value * 2.54))
elif unit == "cm" or unit == "厘米":
    print("{:.1f}厘米为{:.1f}英寸\n".format(value, value / 2.54))
else:
    print("请输入有效的单位！\n")


score = float(input("请输入你的分数："))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "不及格"
print("你的成绩等级为：{}\n".format(grade))


a = float(input("三角型边长a = "))
b = float(input("三角型边长b = "))
c = float(input("三角型边长c = "))
if a + b > c and a + c > b and b + c > a:
    p = a + b + c
    print("该三角形的周长为：{:.1f}".format(p))
    m = p / 2
    area = (m * (m - a) * (m - b) * (m - c)) ** 0.5  # 海伦公式
    print("该三角形的面积为：{:.1f}\n".format(area))
else:
    print("这三条边不能构成三角形！")
