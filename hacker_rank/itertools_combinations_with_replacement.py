"""
See description at https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

You are given a string S.
Your task is to print all possible size k replacement combinations
of the string in lexicographic sorted order.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, n = input().strip().split()

comb = list(combinations_with_replacement(s, int(n)))
comb_sort = [sorted(sublist) for sublist in comb]
comb_concat = list(map("".join, comb_sort))
print(*sorted(comb_concat), sep="\n")
