# from types import MethodType


# class Student(object):
#     pass


# s = Student()
# s.name = 'Micheal'


# def set_age(self, age):
#     self.age = age


# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
# s.set_age(25)
# s.age

# 给一个实例绑定的方法，对另一个实例是不起作用
# s2 = Student()
# s2.set_age(25)


# def set_score(self, score):
#     self.score = score


# Student.set_score = set_score  # 为了给所有实例都绑定方法，可以给class绑定方法

# s.set_score(100)
# s.score
# s2.set_score(100)
# s2.score


# 要限制实例的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = 'Tony'
print(s.name)
s.score = 78



