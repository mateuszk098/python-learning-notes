"""
See description at https://www.hackerrank.com/challenges/np-polynomials
"""

import numpy as np

coeffs = np.array(input().strip().split(), dtype=np.float16)
x = float(input().strip())

print(round(np.polyval(coeffs, x), 1))
