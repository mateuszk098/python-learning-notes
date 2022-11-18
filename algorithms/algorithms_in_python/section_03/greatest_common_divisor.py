"""
Write an algorithm which finds the greatest common divisor (gcd)
of two integers, a and b. Use the Euclidean algorithm.

Description: https://en.wikipedia.org/wiki/Euclidean_algorithm
"""


def gcd(a, b):
    """Recursive version of Euclidean gcd algorithm."""
    if b > a:
        return gcd(a, b - a)
    if a > b:
        return gcd(a - b, b)
    return b


a, b = 24, 30
print(gcd(a, b))
