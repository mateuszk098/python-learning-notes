"""
You have a non-empty set s, and you have to execute N commands given in
N lines. The commands will be pop, remove and discard.

See description at https://www.hackerrank.com/challenges/py-set-discard-remove-pop
"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation, *values = input().split()

    if values:
        values = [int(v) for v in values]

    try:
        getattr(s, operation)(*values)
    except KeyError as e:
        continue

print(sum(s))
