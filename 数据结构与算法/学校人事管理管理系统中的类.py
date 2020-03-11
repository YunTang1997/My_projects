# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/11 14:48
desc: 学校人事管理系统中的类
"""
import datetime


# 派生两个专用的类
class PersonTypeError(TypeError):
    pass


class PersonValueError(ValueError):
    pass

# 公共人员类的实现
class Person(object):
    _num = 0

    # 构造操作
    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) or sex in ("男", "女")):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)  # 如果实参不是合法日期值就会引发异常
        except BaseException:
            raise PersonValueError("Wrong date: ", birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    # 解析操作
    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    # 变动操作
    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name: ", name)
        self._name = name

    def __lt__(self, other):
        if not isinstance(other, Person):
            raise PersonTypeError(other)
        return self._id < other.id()

    @classmethod
    def num(cls):
        return cls._num  # Person._num

    def __str__(self):
        return " ".join((self._id, self._name,
                         self._sex, str(self._birthday), str(self.age())))

    def details(self):
        return " \t".join(("编号：" + self._id,
                           "姓名：" + self._name,
                           "性别：" + self._sex,
                           "出生日期：" + str(self._birthday),
                           "年龄：" + str(self.age())))


# 学生类的实现
class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    # 继承Person类
    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_num)
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}  # 一个空字典

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("No this course selected: ", course_name)
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    # 利用super()函数调用基类的details（）或者Person.details(self)
    def details(self):
        return " \t".join((super().details(),
                           "入学日期：" + str(self._enroll_date),
                           "院系：" + self._department,
                           "课程记录：" + str(self.scores())))

# 教职工类的实现
class Staff(Person):
    _id_num = 0
    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        Person.__init__(self, name, sex, birthday, Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except BaseException:
                raise PersonValueError("Wrong date: ", entry_date)
        else:
            self._entry_date = datetime.date.today()
        self._salary = 1720  # 默认设为最低工资，可修改
        self._department = "未定"  # 需要另行设定
        self._position = "未定"  # 需要另行设定

    def set_salaty(self, amount):
        if not isinstance(amount, int):
            raise TypeError
        self._salary = amount

    def set_positon(self, position):
        if not isinstance(position, str):
            raise TypeError
        self._position = position

    def set_department(self, department):
        if not isinstance(department, str):
            raise TypeError
        self._department = department

    def details(self):
        return " \t".join((super().details(),
                           "入职日期：" + str(self._entry_date),
                           "院系：" + self._department,
                           "职位：" + self._position,
                           "工资：" + str(self._salary)))


if __name__ == '__main__':

    p1 = Person("谢雨洁", "女", (1995, 7, 30), "1201510111")
    p2 = Person("汪力强", "男", (1990, 2, 17), "1201380324")
    p3 = Person("张子玉", "女", (1974, 10, 16), "0197401032")
    p4 = Person("李国栋", "男", (1962, 5, 24), "0196212018")

    plist2 = [p1, p2, p3, p4]
    for p in plist2:
        print(p)

    print("\nAfter sorting: ")
    plist2.sort()  # 调用__lt__(self, other)
    for p in plist2:
        print(p)

    print("提供完整细节信息：")
    for p in plist2:
        print(p.details())

    print("People created: ", Person.num(), "\n")  # 利用类名调用类方法

    p5 = Staff("张子玉", "女", (1974, 10, 16))
    p6 = Staff("李国栋", "男", (1962, 5, 24))

    p5.set_department("数学")
    p5.set_positon("副教授")
    p5.set_salaty(8400)

    print(p5)
    print(p6, "\n")

    print(p5.details())
    print(p6.details(), "\n")
