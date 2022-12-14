"""
See description at https://www.hackerrank.com/challenges/np-array-mathematics
"""

import numpy as np


N, M = list(map(int, input().strip().split()))

l1 = []
for row in range(N):
    l1.append(input().strip().split())

l2 = []
for row in range(N):
    l2.append(input().strip().split())

lnp1 = np.array(l1, dtype=int)
lnp2 = np.array(l2, dtype=int)

print(lnp1 + lnp2)
print(lnp1 - lnp2)
print(lnp1 * lnp2)
print(lnp1 // lnp2)
print(lnp1 % lnp2)
print(lnp1 ** lnp2)
