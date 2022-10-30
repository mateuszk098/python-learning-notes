'''
Eliminate KeyError for dictionaries.
'''

import collections

scores: dict[str, int] = collections.defaultdict(int)
scores['Luisa'] += 1
scores['Etha'] -= 5

print(scores)
