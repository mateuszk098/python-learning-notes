"""
Write an algorithm which calculates the n-th power of a given integer.
Write recursive (natural and with supportive parameter) and iterative versions.
"""


def nth_power_natural(number, power):
    """Recursive version of nth-power."""
    if power == 0:
        return 1
    return number * nth_power_natural(number, power - 1)


def nth_power_with_tmp(number, power, tmp=1):
    """Recursive version of nth-power, with supportive parameter."""
    if power == 0:
        return tmp
    return nth_power_with_tmp(number, power - 1, number * tmp)


def nth_power_iter(number, power):
    """Iterative version of nth-power."""
    if power == 0:
        return number

    tmp = number
    for _ in range(1, power):
        tmp *= number

    return tmp


number = 3
power = 4
print(nth_power_natural(number, power))
print(nth_power_with_tmp(number, power))
print(nth_power_iter(number, power))
