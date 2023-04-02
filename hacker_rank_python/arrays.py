"""
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

See description at https://www.hackerrank.com/challenges/np-arrays
"""

import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(list(reversed(arr)), dtype=float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
