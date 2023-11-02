"""
See description at https://www.hackerrank.com/challenges/np-inner-and-outer
"""

import numpy as np

array1 = np.array(input().strip().split(), dtype=np.int16)
array2 = np.array(input().strip().split(), dtype=np.int16)

print(np.inner(array1, array2))
print(np.outer(array1, array2))
