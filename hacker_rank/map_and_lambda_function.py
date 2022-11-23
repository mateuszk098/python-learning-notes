"""
Let's learn some new Python concepts! You have to generate a list of the
first N fibonacci numbers, 0 being the first number. Then, apply the map
function and a lambda expression to cube each fibonacci number and print
the list.

See description at https://www.hackerrank.com/challenges/map-and-lambda-expression
"""


def cube(x): return x**3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fibons = [0, 1]
    for _ in range(n-2):
        fibons.append(fibons[-2] + fibons[-1])

    return fibons


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
