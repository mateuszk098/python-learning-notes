"""
11 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
"""

# N is always odd and > 5, M is always 3 * N.
N, M = map(int, input().strip().split())

ptrn = ".|."

# The centre has always ".|." pattern.
# Fill both sides of line with (M-3)//2 "-" chars because the ptrn has 3 chars.
for i in range(N//2):
    print((ptrn*i).rjust((M-3)//2, "-") + ptrn + (ptrn*i).ljust((M-3)//2, "-"))

print("WELCOME".center(M, "-"))

for i in range(N//2 - 1, -1, -1):
    print((ptrn*i).rjust((M-3)//2, "-") + ptrn + (ptrn*i).ljust((M-3)//2, "-"))
