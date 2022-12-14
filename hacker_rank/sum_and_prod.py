"""
You are given a 2-D array with dimensions NXM.
Your task is to perform the sum tool over axis 0 and then find 
the product of that result.

See description at https://www.hackerrank.com/challenges/np-sum-and-prod
"""


import numpy as np


N, M = list(map(int, input().strip().split()))

l = []
for _ in range(N):
    l.append(list(map(int, input().strip().split())))

lnp = np.array(l)
lprod = np.sum(lnp, axis=0).prod()
print(lprod)
