# 继承(方法)
class Animal(object):
    def run(self):
        print('Animal is running.')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()


a = Animal()
b = Dog()

# 多态
isinstance(a, Animal)
isinstance(a, Dog)
isinstance(b, Dog)
isinstance(b, Animal)


class Parent(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def print_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Child(Parent):
    pass


parent = Parent('CCC', 48)
# child = Child()  报错,子类仅继承了父类的方法
# child = Child('AAA', 18)




