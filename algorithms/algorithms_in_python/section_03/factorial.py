"""
Write an algorithm which calculates the factorial of n.
Write recursive and iterative versions.

Description: https://en.wikipedia.org/wiki/Factorial
"""


def factorial_rec(n):
    """Recursive version of factorial."""
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


def factorial_iter(n):
    """Iterative version of factorial."""
    if n == 0:
        return 1

    tmp = 1
    for number in range(1, n + 1):
        tmp *= number

    return tmp


n = 6
print(f"{n}! = {factorial_rec(n)}")
print(f"{n}! = {factorial_iter(n)}")
