"""
See description at: https://www.hackerrank.com/challenges/defaultdict-tutorial

In this challenge, you will be given 2 integers, n and m. There are n words, 
which might repeat, in word group A. There are m words belonging to word group B. 
For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().strip().split())

A = defaultdict(list)
for index in range(n):
    A[input()].append(index+1)

for _ in range(m):
    print(*A.get(input(), [-1]))
