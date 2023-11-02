"""
Perform append, pop, popleft and appendleft methods on an empty deque d.

See description at https://www.hackerrank.com/challenges/py-collections-deque
"""


from collections import deque

n = int(input().strip())
d = deque()

for _ in range(n):

    operation, *values = input().strip().split()

    if operation == "append":
        d.append(int(values[0]))
    elif operation == "appendleft":
        d.appendleft(int(values[0]))
    elif operation == "pop":
        d.pop()
    elif operation == "popleft":
        d.popleft()

    # getattr(d, operation)(*values)

print(*d, sep=" ")
