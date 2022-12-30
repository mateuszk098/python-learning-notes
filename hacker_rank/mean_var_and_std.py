"""
See description at https://www.hackerrank.com/challenges/np-mean-var-and-std
"""

import numpy as np

n, m = input().strip().split()
n, m = int(n), int(m)


matrix = np.empty((n, m), dtype=np.int16)
for row in range(n):
    matrix[row, :] = list(map(int, input().split()))

print(np.mean(matrix, axis=1))
print(np.var(matrix, axis=0))
print(round(np.std(matrix), 11))
