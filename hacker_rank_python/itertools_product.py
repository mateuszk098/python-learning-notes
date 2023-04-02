"""
See description at https://www.hackerrank.com/challenges/itertools-product

You are given two lists A and B. Your task is to compute their cartesian product AxB.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

prod = list(product(A, B))
print(*prod)
