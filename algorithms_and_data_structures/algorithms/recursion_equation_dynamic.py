"""
Solve the following recursion equation using dynamic programming.

P(i,j) = 1                              i = 0, j > 0;
P(i,j) = 0                              i > 0, j = 0;
P(i,j) = [P(i-1,j) + P(i,j-1)] / 2      i > 0, j > 0;

Idea - create inital array like the following.

  j  0  1  2  3  4
i
0    0  1  1  1  1
1    0  0  0  0  0
2    0  0  0  0  0
3    0  0  0  0  0
4    0  0  0  0  0

Then follow the P(i,j) formula.
"""

from math import isclose  # Assertion for float pointing numbers.

import numpy as np


def equation_solver(i, j, array_show=False):
    """Returns P(i,j) value."""
    array = np.zeros((i + 1, j + 1), dtype=np.float32)
    array[0] = 1
    array[0][0] = 0

    for row in range(1, i + 1):
        for col in range(1, j + 1):
            array[row, col] = (array[row - 1][col] + array[row][col - 1]) / 2.

    if array_show:
        print(array)

    return array[i, j]


assert isclose(equation_solver(4, 4, True), 0.5)
assert isclose(equation_solver(3, 4), 0.65625)
