"""
You are given a set A and n other sets. Your job is to find
whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets.
Otherwise, print False. 

A strict superset has at least one element that does not exist in its subset.

See description at https://www.hackerrank.com/challenges/py-check-strict-superset
"""

a = set(map(int, input().split()))
cases = int(input())
tmp = []

for _ in range(cases):
    b = set(map(int, input().split()))
    tmp.append(a.issuperset(b))

print(all(tmp))
