import math

class Rational:
    def __init__(self, numerator = 1, denominator = 1):
        self.__check(numerator, denominator)

        divisor = math.gcd(numerator, denominator)
        self.__numerator = numerator // divisor
        self.__denominator = denominator // divisor

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def __check(self, n, d):
        if not d:
            raise ZeroDivisionError('Division by 0')
        if not (isinstance(n, int) and isinstance(d, int)):
            raise TypeError('Wrong value type')

    @property
    def float(self):
        return self.__numerator / self.__denominator

    def __add__(self, other):
        lcm = math.lcm(self.__denominator, other.__denominator)
        self_numerator = int(self.__numerator * (lcm / self.__denominator))
        other_numerator = int(other.__numerator * (lcm / other.__denominator))
        return Rational(self_numerator + other_numerator, lcm)

    def __sub__(self, other):
        lcm = math.lcm(self.__denominator, other.__denominator)
        self_numerator = int(self.__numerator * (lcm / self.__denominator))
        other_numerator = int(-(other.__numerator * (lcm / other.__denominator)))
        return Rational(self_numerator + other_numerator, lcm)

    def __mul__(self, other):
        return Rational(self.__numerator * other.__numerator,
                        self.__denominator * other.__denominator)

    def __truediv__(self, other):
        return Rational(self.__numerator * other.__denominator,
                        self.__denominator * other.__numerator)

    def __lt__(self, other):
        return self.float < other.float
    
    def __gt__(self, other):
        return self.float > other.float

    def __le__(self, other):
        return self.float <= other.float

    def __ge__(self, other):
        return self.float >= other.float

    def __eq__(self, other):
        return self.float == other.float

    def __ne__(self, other):
        return self.float != other.float

r1 = Rational(6, 2)
r2 = Rational(5, 2)

print(r1 + r2)
print(r2 - r1)
print(r1 * r2)
print(r1 / r2)

print(r1 < r2)
print(r2 > r1)
print(r1 <= r2)
print(r1 >= r2)
print(r1 == r2)
print(r2 != r1)
