"""
Example of the Longest Common Subsequence algorithm with dynamic programming.

Time complexity: O(n*m), where n is the length of the first sequence, 
and m is the length of the second sequence.
"""

import numpy as np


def lcs_length(sequence1, sequence2, show_subseq=False, show_matrix=False):
    """Returns length of the longest common subsequence for two sequences."""
    n, m = len(sequence1), len(sequence2)
    matrix = np.zeros((n + 1, m + 1), dtype=np.int16)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])

    if show_matrix:
        print(matrix)

    if show_subseq:
        print(_lcs_sequence(sequence1, sequence2, matrix, n, m))

    return matrix[n][m]


def _lcs_sequence(sequence1, sequence2, matrix, i, j):
    """Returns longest common subsequence."""
    if i == 0 or j == 0:
        return ""
    if sequence1[i - 1] == sequence2[j - 1]:
        return _lcs_sequence(sequence1, sequence2, matrix, i - 1, j - 1) + sequence1[i - 1]
    if matrix[i][j - 1] > matrix[i - 1][j]:
        return _lcs_sequence(sequence1, sequence2, matrix, i, j - 1)
    return _lcs_sequence(sequence1, sequence2, matrix, i - 1, j)


assert lcs_length("abc", "act", True, True) == 2  # ac
assert lcs_length("pcaytek", "mcjaieoti") == 3  # cat
assert lcs_length("cahiuemetrdavbfgh", "hchzeeotmnbah", True) == 7  # cheetah
