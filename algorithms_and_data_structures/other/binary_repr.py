"""
Write an algorithm which prints the binary representation of the given integer.
Write recursive and iterative versions.

Description: https://en.wikipedia.org/wiki/Binary_number
"""


def binary_repr_rec(n):
    """Recursive version of binary representation of given integer."""
    if n < 1:
        return 0
    if n > 0:
        binary_repr_rec(n // 2)
    print(n % 2, end="")


def binary_repr_iter(n):
    """Iterative version of binary representation of given integer."""
    if n < 1:
        return 0

    lst = []
    while n > 0:
        lst.append(str(n % 2))
        n = n // 2

    lst.reverse()
    print("".join(lst))


n = 8
binary_repr_rec(n)
print()
binary_repr_iter(n)
