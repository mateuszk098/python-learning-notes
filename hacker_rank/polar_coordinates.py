"""
You are given a complex z. Your task is to convert it to polar coordinates.

See description at https://www.hackerrank.com/challenges/polar-coordinates
"""

import cmath

z = complex(input().strip())
r, phi = cmath.polar(z)
print(r, phi, sep="\n")
