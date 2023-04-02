"""
See description at https://www.hackerrank.com/challenges/np-linear-algebra
"""

import numpy as np
import numpy.linalg as linalg

n = int(input().strip())
matrix = np.empty((n, n))

for row in range(n):
    matrix[row, :] = input().split()

print(round(linalg.det(matrix), 2))
