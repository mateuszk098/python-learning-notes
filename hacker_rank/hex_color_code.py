"""
See description at https://www.hackerrank.com/challenges/hex-color-code
"""

import re

for _ in range(int(input())):
    s = input()
    if re.search(r"^\s.*(#[\da-fA-F]{3,6})", s):
        print(*re.findall(r"#[\da-fA-F]{3,6}", s), sep="\n")
