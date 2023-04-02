"""
See description at https://www.hackerrank.com/challenges/find-angle
"""

import math

ab = int(input().strip())
bc = int(input().strip())

mc = 0.5 * math.sqrt(ab*ab + bc*bc)
mb = mc  # In such a problem mb is always equal to mc.

# Cosine formula mb^2 + bc^2 - 2*mb*bc*cos(t) = mc^2

theta = math.acos((mb*mb + bc*bc - mc*mc) / (2*mb*bc))
print(f"{math.degrees(theta):.0f}\u00b0")
