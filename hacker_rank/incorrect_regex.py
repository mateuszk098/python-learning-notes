"""
You are given a string S.
Your task is to find out whether S is a valid regex or not.

See description at https://www.hackerrank.com/challenges/incorrect-regex
"""

import re

n = int(input().strip())

for _ in range(n):
    tmp = input().strip()
    try:
        re.compile(tmp)
    except re.error as err:
        print(False)
    else:
        print(True)
