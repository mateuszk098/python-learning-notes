"""
See description at https://www.hackerrank.com/challenges/maximize-it
"""

from itertools import product


N, M = map(int, input().strip().split())
values = []

for _ in range(N):
    tmp = list(map(int, input().strip().split()))
    # [1:] because the first element is list size...
    tmp = [x*x for x in tmp[1:]]
    values.append(tmp)

# We need all combinations of values from nested lists.
prods = list(product(*values))
max_prods = [sum(x) % M for x in prods]
result = max(max_prods)

print(result)
