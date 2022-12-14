"""
Your task is to print an array of size NXM with its main diagonal
elements as 1's and 0's everywhere else.

See description at https://www.hackerrank.com/challenges/np-eye-and-identity
"""

import numpy as np
np.set_printoptions(legacy="1.13")

N, M = list(map(int, input().strip().split()))
eye = np.eye(N, M)
print(eye)
