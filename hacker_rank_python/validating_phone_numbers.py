"""
See description at https://www.hackerrank.com/challenges/validating-the-phone-number
"""

import re

cases = int(input().strip())
pattern = re.compile(r"[7-9]\d{9}$")

for _ in range(cases):
    number = input().strip()
    if pattern.match(number):
        print("YES")
    else:
        print("NO")
