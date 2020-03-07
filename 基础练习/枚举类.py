from enum import Enum, unique


Month = Enum('Month', ('Jan', 'Fed', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member,  ',', member.value)  # value属性自动赋给成员int常量，默认从1开始计数
# print(Month.Jan.value)


@unique  # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday(1))
print(Weekday.Wed.value)
for date in Weekday:
    print(date.name, '=>', date, ',', date.value)


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender(0))
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
