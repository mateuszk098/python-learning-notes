"""
See description at https://www.hackerrank.com/challenges/re-start-re-end
"""

import re

s = input().strip()
k = input().strip()

pattern = rf"(?=({k}))"
result = re.finditer(pattern, s)

ids = [(group.start(), group.end() + len(k) - 1) for group in result]
if ids:
    for group in ids:
        print(group)
else:
    print("(-1, -1)")
