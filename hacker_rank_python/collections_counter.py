"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x_i amount
of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.

See description at https://www.hackerrank.com/challenges/collections-counter
"""

# I don't have any idea where to use Counter here and why?

X = int(input().strip())
sizes = list(map(int, input().strip().split()))
N = int(input().strip())

result = 0
for _ in range(N):
    size, price = map(int, input().strip().split())
    if size in sizes:
        result += price
        sizes.remove(size)

print(result)
