"""
See description at https://www.hackerrank.com/challenges/introduction-to-regex
"""

import re


cases = int(input().strip())
pattern = re.compile(r"[+-]?\d*\.\d+$")

for _ in range(cases):
    s = input().strip()
    if pattern.match(s):
        print(True)
    else:
        print(False)
