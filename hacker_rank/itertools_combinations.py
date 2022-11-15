"""
See description at https://www.hackerrank.com/challenges/itertools-combinations

You are given a string S.
Your task is to print all possible combinations, up to size k, of the string
in lexicographic sorted order.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, n = input().strip().split()

for k in range(1, int(n)+1):
    comb = list(combinations(s, k))
    comb_sort = [sorted(sublist) for sublist in comb]
    comb_concat = list(map(''.join, comb_sort))
    print(*sorted(comb_concat), sep='\n')
