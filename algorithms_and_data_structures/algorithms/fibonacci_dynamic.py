"""
Example of fibonacci nth number calculation with dynamic programming.
"""


def nth_fibonacci_number(n):
    """Return list with `n` fibonacci numbers."""
    if n <= 2:
        return [0, 1]

    numbers = [0] * (n + 1)
    numbers[1] = 1
    for i in range(2, n + 1):
        numbers[i] = numbers[i - 1] + numbers[i - 2]

    return numbers


assert nth_fibonacci_number(8) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
assert nth_fibonacci_number(124)[124] == 36726740705505779255899443
