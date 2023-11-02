"""
See description at https://www.hackerrank.com/challenges/np-dot-and-cross
"""

import numpy as np

n = int(input().strip())

matrix1 = np.empty((n, n), dtype=np.int16)
matrix2 = np.empty((n, n), dtype=np.int16)

for row in range(n):
    matrix1[row, :] = input().split()

for row in range(n):
    matrix2[row, :] = input().split()

print(matrix1.dot(matrix2))
