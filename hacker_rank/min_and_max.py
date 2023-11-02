"""
See description at https://www.hackerrank.com/challenges/np-min-and-max
"""

import numpy as np

n, m = input().strip().split()
n, m = int(n), int(m)


matrix = np.empty((n, m), dtype=np.int16)
for row in range(n):
    matrix[row, :] = list(map(int, input().split()))

axis1_min = np.min(matrix, axis=1)
print(max(axis1_min))
