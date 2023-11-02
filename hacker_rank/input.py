"""
You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) = k.

See description at https://www.hackerrank.com/challenges/input
"""

x, k = map(int, input().strip().split())
func = input().strip()

if eval(func) == k:
    print(True)
else:
    print(False)
