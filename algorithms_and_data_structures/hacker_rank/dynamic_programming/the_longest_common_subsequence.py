"""
https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence
"""


def lcs(a, b):
    # Write your code here
    n, m = len(a), len(b)
    matrix = [0] * (n + 1)
    for i in range(n + 1):
        matrix[i] = [0] * (m + 1)  # type: ignore

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1  # type: ignore
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])  # type: ignore

    return _lcs_pattern(a, b, matrix, n, m)


def _lcs_pattern(a, b, matrix, i, j):
    """Internal use. Returns the longest common subsequence of `a` and `b`."""
    if i == 0 or j == 0:
        return " "
    if a[i - 1] == b[j - 1]:
        return _lcs_pattern(a, b, matrix, i - 1, j - 1) + a[i - 1] + " "
    if matrix[i][j - 1] > matrix[i - 1][j]:
        return _lcs_pattern(a, b, matrix, i, j - 1)
    return _lcs_pattern(a, b, matrix, i - 1, j)


if __name__ == '__main__':
    dummy = input()  # Length of the a and b - unnecessary in Python.
    a = input().strip().split()
    b = input().strip().split()
    print(lcs(a, b))
