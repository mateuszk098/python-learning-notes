"""
See description at https://www.hackerrank.com/challenges/introduction-to-regex
"""

import re

N = int(input().strip())

pattern = r"""
    [-+.]?  # Is there a - or + or . at the beginning?
    \d*     # Is there 0 or more digits?
    \.      # Is a dot between digits?
    \d+$    # Must end with 1 or more digits.
"""
pattern_comp = re.compile(pattern, flags=re.VERBOSE)

for _ in range(N):
    number = input().strip()
    if pattern_comp.match(number):
        print(True)
    else:
        print(False)
