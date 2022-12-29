"""
Example of the Longest Common Substring algorithm with dynamic programming.

Time complexity: O(n*m), where n is the length of the first sequence, 
and m is the length of the second sequence.
"""

import numpy as np


def lcs_length(sequence1, sequence2, show_substring=False, show_matrix=False):
    """Returns length of the longest common substring for two sequences."""
    result_length = 0
    n, m = len(sequence1), len(sequence2)
    matrix = np.zeros((n + 1, m + 1), dtype=np.int16)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                matrix[i, j] = matrix[i - 1, j - 1] + 1
                result_length = max(result_length, matrix[i, j])

    if show_matrix:
        print(matrix)

    if show_substring:
        print(_lcs_sequence(sequence1, sequence2, matrix, n, m))

    return result_length


def _lcs_sequence(sequence1, sequence2, matrix, n, m):
    """Returns longest common substring for two sequences."""
    result_length = 0
    substring = ""
    row, col = 0, 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                if result_length < matrix[i, j]:
                    result_length = matrix[i, j]
                    row, col = i, j

    if result_length != 0:
        while matrix[row][col] != 0:
            substring += sequence1[row - 1]  # Create substring from right to left.
            row -= 1
            col -= 1
        return substring[::-1]  # From left to right.

    return ""


assert lcs_length("abcdefg", "def", True, True) == 3  # def
assert lcs_length("pieski jest ten świat", "kot i pies śpią obok siebie") == 4  # pies
