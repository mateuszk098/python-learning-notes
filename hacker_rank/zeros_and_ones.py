"""
You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions, your task is to
print an array of the given shape and integer type using the tools
`numpy.zeros` and `numpy.ones`.

See description at https://www.hackerrank.com/challenges/np-zeros-and-ones
"""

import numpy as np


shape = list(map(int, input().strip().split()))

zeros = np.zeros(shape, dtype=int)
ones = np.ones(shape, dtype=int)

print(zeros)
print(ones)
