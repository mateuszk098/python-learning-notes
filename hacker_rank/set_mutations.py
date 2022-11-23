"""
You are given a set A and N number of other sets. These N number of sets
have to perform some specific mutation operations on set A. Your task is
to execute those operations and print the sum of elements from set A.

See description at https://www.hackerrank.com/challenges/py-set-mutations
"""

alen = int(input())
a = set(map(int, input().split()))
operations = int(input())

for _ in range(operations):
    operation, blen = input().split()
    b = set(map(int, input().split()))
    getattr(a, operation)(b)

print(sum(a))
