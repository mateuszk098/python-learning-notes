"""
You are given a NXM integer array matrix with space separated
elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.

See description at https://www.hackerrank.com/challenges/np-transpose-and-flatten
"""

import numpy as np

N, M = list(map(int, input().strip().split()))

l = []
for row in range(N):
    l.append(input().strip().split())

lnp = np.array(l, dtype=int)
print(lnp.transpose())
print(lnp.flatten())
