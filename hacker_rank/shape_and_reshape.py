"""
You are given a space separated list of nine integers.
Your task is to convert this list into a 3X3 NumPy array.

See description at https://www.hackerrank.com/challenges/np-shape-reshape/
"""

import numpy as np


l = list(map(int, input().strip().split()))
lnp = np.array(l).reshape((3, 3))
print(lnp)
