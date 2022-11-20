"""
Read in two integers, a and b, and print three lines.
The first line is the integer division.
The second line is the result of the modulo operator: a % b.
The third line prints the divmod of a and b.

See description at https://www.hackerrank.com/challenges/python-mod-divmod
"""

a, b = int(input().strip()), int(input().strip())

print(a // b)
print(a % b)
print(divmod(a, b))
