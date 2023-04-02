"""
You are given a 1-D array, A. Your task is to print the floor, ceil and
rint of all the elements of A.

See description at https://www.hackerrank.com/challenges/floor-ceil-and-rint
"""

import numpy as np
np.set_printoptions(legacy="1.13")

l = input().strip().split()
lnp = np.array(l, dtype=float)

print(np.floor(lnp))
print(np.ceil(lnp))
print(np.rint(lnp))
