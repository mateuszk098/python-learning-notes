"""
See description at https://www.hackerrank.com/challenges/piling-up
"""

n = int(input().strip())

for _ in range(n):
    dummy = input()
    d = list(map(int, input().strip().split()))
    can_stack = True
    top = max(d[0], d[-1])
    l, r = 0, len(d) - 1

    while l < r:
        if d[l] >= d[r]:
            newtop = d[l]
            l += 1
        else:
            newtop = d[r]
            r -= 1

        if newtop > top:
            can_stack = False
            break

        top = newtop

    if can_stack:
        print("Yes")
    else:
        print("No")
