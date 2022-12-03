"""
Write an algorithm to check if the given number is prime.

Description: https://en.wikipedia.org/wiki/Prime_number
"""


from math import sqrt


def is_prime(n):
    """
    If a number n is not a prime, it can be factored into two factors
    x and y, e.g. n = x * y. Numbers x and y can't be both greater than the
    square root of n. So in any factorization of n, at least one of the
    factors must be smaller than the square root of n.
    """
    if n < 2:
        return False

    tmp: int = int(sqrt(n)) + 1
    for number in range(2, tmp):
        if n % number == 0:
            return False

    return True


for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")
