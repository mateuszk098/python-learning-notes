def my_sum(a, b):
    return a + b


def my_diff(a, b):
    return a - b


def my_prod(a, b):
    return a * b


def my_quot(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
