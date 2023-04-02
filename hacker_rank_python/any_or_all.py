"""
You are given a space separated list of integers. If all the integers
are positive, then you need to check if any integer is a palindromic integer.

See description at https://www.hackerrank.com/challenges/any-or-all
"""

dummy = input()
numbers = list(map(int, input().split()))

if all(value > 0 for value in numbers) and any(str(value) == str(value)[::-1] for value in numbers):
    print(True)
else:
    print(False)
