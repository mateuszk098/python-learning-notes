"""
You are given a spreadsheet that contains a list of N athletes and their
details (such as age, height, weight and so on). You are required to sort
the data based on the k-th attribute and print the final resulting table.

See description at https://www.hackerrank.com/challenges/python-sort-sort
"""

n, m = map(int, input().split())
athletes = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

athletes.sort(key=lambda x: x[k])
for attributes in athletes:
    print(*attributes)
