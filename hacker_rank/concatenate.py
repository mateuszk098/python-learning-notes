"""
You are given two integer arrays of size NXP and MXP (N & M are rows,
and P is the column). Your task is to concatenate the arrays along axis 0.

See description at https://www.hackerrank.com/challenges/np-concatenate
"""

import numpy as np

N, M, P = list(map(int, input().strip().split()))

l1 = []
for row in range(N):
    l1.append(input().strip().split())

l2 = []
for row in range(M):
    l2.append(input().strip().split())

arr = np.concatenate((np.array(l1, dtype=int), np.array(l2, dtype=int)), axis=0)
print(arr)
