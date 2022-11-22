"""
You are the manager of a supermarket. You have a list of N items
together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its
first occurrence.

See description at https://www.hackerrank.com/challenges/py-collections-ordereddict
"""


from collections import OrderedDict

N = int(input().strip())
orders = OrderedDict()

for _ in range(N):
    item, sep, price = input().rpartition(" ")
    orders[item] = orders.get(item, 0) + int(price)

for key, value in orders.items():
    print(key, value)
