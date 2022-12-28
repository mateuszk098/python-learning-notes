"""
Example of greedy algorithm.

You have a descending sorted list of denominations. Write an algorithm,
which calculates how much money the shop assistant must spend to the customer.
Suppose the custom bought an item, which costs `x` and paid `y`. Suppose, that
there is always money in the cash register.
"""

DENOMINATIONS = [100, 50, 20, 10, 5, 2, 1]


def remainder(customer_amount, item_price):
    """Returns dictionary with denomination-counts (key-value) pairs."""
    index = 0
    remain = customer_amount - item_price
    denominations_to_spend = {}

    while remain > 0:
        denomination = DENOMINATIONS[index]
        if remain >= denomination:
            counts = remain // denomination
            remain -= counts * denomination
            denominations_to_spend[denomination] = counts
        index += 1

    return denominations_to_spend


assert remainder(100, 9) == {50: 1, 20: 2, 1: 1}
assert remainder(50, 12) == {20: 1, 10: 1, 5: 1, 2: 1, 1: 1}
assert remainder(10, 10) == {}
