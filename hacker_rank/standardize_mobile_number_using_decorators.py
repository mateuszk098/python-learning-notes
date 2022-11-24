"""
See description at https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators
"""


def wrapper(print_sorted):
    def inner(numbers):
        # complete the function
        lst = [f"+91 {number[-10:-5]} {number[-5:]}" for number in numbers]
        print_sorted(lst)
    return inner


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
