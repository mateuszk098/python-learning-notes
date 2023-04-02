"""
See description at https://www.hackerrank.com/challenges/re-group-groups
"""

import re

s = input()
pattern = r"([a-zA-Z0-9])\1+"
match = re.search(pattern, s)
if match:
    print(match.group(1))
else:
    print(-1)
