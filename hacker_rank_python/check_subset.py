"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

See description at https://www.hackerrank.com/challenges/py-check-subset
"""

cases = int(input())

for _ in range(cases):
    dummy = input()
    a = set(map(int, input().split()))
    dummy = input()
    b = set(map(int, input().split()))
    print(a.issubset(b))
