"""
See description at https://www.hackerrank.com/challenges/re-findall-re-finditer
"""

import re

s = input().strip()
pattern = r"(?<=[^aeiou])([aeiou]{2,})[^aeiou]"
result = re.findall(pattern, s, flags=re.IGNORECASE)

if not result:
    print(-1)
else:
    print(*result, sep="\n")
