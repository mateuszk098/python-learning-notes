"""
5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

import copy


def print_rangoli(size):
    # your code goes here
    """
    The line is splitted into 3 parts.
    The middle part of line is always "-chr(x)-", e.g. "-e-", and it reserves 3 fields.
    The left and right parts always have (N-1) letters and (N-2) "-" characters.
    So in the left and right part of the line remains `space` fields.
    """
    middle_line_chars = (size-1)*2 + (size-2)*2 + 3
    space = (middle_line_chars-3)//2

    lptrn = ""
    rptrn = ""
    up_patterns = []

    for k in range(1, size+1):
        pattern = lptrn.rjust(space, "-") + f"-{chr(97+size-k)}-" + rptrn.ljust(space, "-")
        up_patterns.append(pattern)
        lptrn = lptrn + f"-{chr(97+size-k)}"
        rptrn = f"{chr(97+size-k)}-" + rptrn

    up_patterns[-1] = up_patterns[-1].strip("-")  # Remove "-" from middle line edges.
    bottom_patterns = copy.copy(up_patterns)
    bottom_patterns.pop()  # Remove the middle line.
    bottom_patterns.reverse()

    patterns = up_patterns + bottom_patterns
    for line in patterns:
        print(line)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
