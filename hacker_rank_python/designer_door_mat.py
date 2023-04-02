"""
See description at https://www.hackerrank.com/challenges/designer-door-mat

Mr. Vincent works in a door mat manufacturing company. One day, he designed 
a new door mat with the following specifications:

* Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
* The design should have 'WELCOME' written in the center.
* The design pattern should only use |, . and - characters.

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
