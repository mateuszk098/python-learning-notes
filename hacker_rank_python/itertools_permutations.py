"""
See description at https://www.hackerrank.com/challenges/itertools-permutations

You are given a string S.
Your task is to print all possible permutations of size k of the string
in lexicographic sorted order.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, k = input().strip().split()

perm = list(permutations(s, int(k)))
perm_concat = list(map("".join, perm))

print(*sorted(perm_concat), sep="\n")
