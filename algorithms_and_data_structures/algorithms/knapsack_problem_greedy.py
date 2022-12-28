"""
Example of greedy algorithm.
See https://en.wikipedia.org/wiki/Knapsack_problem

Given a set of items, each with a weight, value, counts and labels. 
Determine the number of each item to include in a collection so that
the total weight is less than or equal to a given limit and the total value 
is as large as possible.
"""

from collections import defaultdict


def knapsack(values, weights, counts, labels, limit):
    """Returns dictionary where each key is the item label and the value
    is the number of items to take."""
    remain_to_fill = limit
    # The most optimal items are that ones the ratio value / weight is the largest.
    elements = list(zip(values, weights, counts, labels))
    elements.sort(key=lambda x: x[0] / x[1], reverse=True)

    index = 0
    elements_to_take = defaultdict(int)
    while index < len(elements):
        value, weight, count, label = elements[index]
        to_take = remain_to_fill // weight  # How many these items we can take.
        if remain_to_fill <= 0 or count == 0 or to_take == 0:
            break
        # We take as many items as possible.
        if to_take < count:
            elements_to_take[label] += to_take
            remain_to_fill -= to_take * weight
        else:
            elements_to_take[label] += count
            remain_to_fill -= count * weight
        index += 1

    return elements_to_take


values1 = [1, 2, 4, 3, 1, 5]
weights1 = [3.5, 2.5, 2, 1, 4, 1.5]
counts1 = [4, 5, 1, 2, 3, 2]
labels1 = ["a", "b", "c", "d", "e", "f"]
assert knapsack(values1, weights1, counts1, labels1, 10) == {"f": 2, "d": 2, "c": 1, "b": 1}

values2 = [3, 4, 5]
weights2 = [3, 2, 1]
counts2 = [2, 10, 3]
labels2 = ["a", "b", "c"]
assert knapsack(values2, weights2, counts2, labels2, 20) == {"c": 3, "b": 8}
