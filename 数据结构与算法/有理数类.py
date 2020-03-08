class Rational:
    #  定义一个静态方法，求解最大公约数
    @staticmethod
    def __gcd(m, n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n

    #  初始化方法
    def __init__(self, num, den=1):
        #  判断分子、分母是否均为整数
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        #  判断分母是否为0
        if den == 0:
            raise ZeroDivisionError
        #  将有理数标准化
        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational.__gcd(num, den)
        #  定义内部属性
        self.__num = sign * (num // g)
        self.__den = den // g
    #  通过解析方法（解析函数），使得在类外部同样可以调用有理数的分子和分母

    def num(self):
        return self.__num

    def den(self):
        return self.__den
    #  定义有理数基本计算方法

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        num = self.__num * other.den() + self.__den * other.num()
        den = self.__den * other.den()
        return Rational(num, den)

    def __sub__(self, other):
        if not isinstance(oyher, Rational):
            raise TypeError
        num = self.__num * other.den() - self.__den * other.num()
        den = self.__den * other.den()
        return Rational(num, den)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        return Rational(self.__num * other.num(),
                        self.__den * other.den())

    def __floordiv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        if other.num() == 0:
            raise ZeroDivisionError
        return Rational(self.__num * other.den(),
                        self.__den * other.num())
    #  大小关系

    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        return self.__num * other.den() == self.__den * other.num()

    def __ne__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        return self.__num * other.den() != self.__den * other.num()

    def __lt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        return self.__num * other.den() < self.__den * other.num()

    def __le__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        return self.__num * other.den() <= self.__den * other.num()

    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        return self.__num * other.den() > self.__den * other.num()

    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        return self.__num * other.den() >= self.__den * other.num()

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def print(self):
        print(self.__num, "/", self.__den)


if __name__ == '__main__':
    five = Rational(5)
    five.print()
    x = Rational(3, 5)
    x.print()
    print("Two thirds are", Rational(2, 3))
    y = five + x * Rational(5, 17)
    y.print()
    print(Rational(1, 2) == Rational(2, 3))
    print(Rational(1, 2) >= Rational(2, 3))
    print(Rational(1, 2) <= Rational(2, 3))
    print(Rational(1, 2) != Rational(1, 2))
