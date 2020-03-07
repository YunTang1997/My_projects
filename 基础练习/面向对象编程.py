# std1 = {'name': 'Micheal', 'score': 98}
# std2 = {'name': 'Bob', 'score': 81}
#
#
# def print_score(std):
#     print('%s: %s' % (std['name'], std['score']))
#
#
# print_score(std1)


# class Student(object):
#     """__init__方法的第一个参数永远是self，表示创建的实例本身"""
#     """如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__"""
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#     """类的方法"""
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_grade(self):
#         if self.__score >= 90:
#             return 'A'
#         elif self.__score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
#     """外部代码要获取name和score"""
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     """如果又要允许外部代码修改score怎么办"""
#     def set_score(self, score):
#         self.__score = score


# 创建实例
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# 即使__name是私有变量，但是仍然可以通过_Student__name访问name，但是强烈不建议这么干
# bart._Student__name
# 调用方法
# bart.print_score()
# lisa.print_score()
# print(bart.get_name() + ': ' + bart.get_grade())


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError('bad value')


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

