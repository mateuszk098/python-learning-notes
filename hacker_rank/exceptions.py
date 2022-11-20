"""
You are given two values a and b.
Perform integer division and print a / b.

See description at https://www.hackerrank.com/challenges/exceptions
"""

n = int(input().strip())

for _ in range(n):
    try:
        a, b = list(map(int, input().strip().split()))
        res = a // b
    except (ZeroDivisionError, ValueError) as err:
        print("Error Code:", err)
    else:
        print(res)
