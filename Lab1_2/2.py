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

    def float(self):
        return self.__numerator / self.__denominator