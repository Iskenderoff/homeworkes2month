
from math import gcd

class My_fraction:

    def __init__(self, numerator, denominator=1):
        self._num = numerator
        self._den = denominator
        g = gcd(self._num, self._den)
        self._num //= g
        self._den //= g
        is_neg = self._num * self._den < 0
        self._den = abs(self._den)
        self._num = abs(self._num)
        if is_neg:
            self._num *= -1


    def __add__(self, other):
        a = self._num
        b = self._den
        c = other._num
        d = other._den
        return My_fraction(a*d + b*c, b*d)


    def __sub__(self, other):
        a = self._num
        b = self._den
        c = other._num
        d = other._den
        return My_fraction(a * d - b * c, b * d)


    def __mul__(self, other):
        a = self._num
        b = self._den
        c = other._num
        d = other._den
        return My_fraction(a * c, b * d)


    def __floordiv__(self, other):

        a = self._num
        b = self._den
        c = other._num
        d = other._den
        return My_fraction(a * d, b * c)


    def __str__(self):
        return str(self._num) + '/' + str(self._den)


a = My_fraction(2, -3)
b = My_fraction(4, 5)
print(f'a = {a}')
print(f'b = {b}')
print(f'a + b = {a+b}')
print(f'a - b = {a-b}')
print(f'a * b = {a*b}')
print(f'a // b = {a//b}')

