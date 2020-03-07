# class Student(object):
#     __slots__ = ('name', '__score')
#
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         elif value < 0 or value > 100:
#             raise ValueError('score must between 0~100!')
#         else:
#             self.__score = value


# s = Student('Tony', 98)
# # s.name
# # s.get_score()
# # s.set_score('a')

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        elif value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        else:
            self._score = value


s = Student()
s.score = 60  # OK,实际转化为s.set_score(60)
s.score  # OK,实际转化为s.get_score()
s.score = 999


class Screen(object):
    @property  # 将方法变成一个属性
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError('width must be greater than 0!')
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError('height must be greater than 0!')
        else:
            self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
