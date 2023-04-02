"""
For this challenge, you are given two complex numbers, and you have
to print the result of their addition, subtraction, multiplication,
division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

See description at https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers
"""


import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imag = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imag)

    def __truediv__(self, no):
        real_num = self.real * no.real + self.imaginary * no.imaginary
        imag_num = self.imaginary * no.real - self.real * no.imaginary
        denominator = no.real * no.real + no.imaginary * no.imaginary
        real = real_num / denominator
        imag = imag_num / denominator
        return Complex(real, imag)

    def mod(self):
        modulus = math.sqrt(self.real * self.real + self.imaginary * self.imaginary)
        # Such operation does not have any sense.
        return Complex(modulus, 0)  # Should normal be - return modulus

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
