'''
Print list with indices.
'''

names: list[str] = ["Corey", "David", "Chris", "Travis"]

# Weak solution
index: int = 0
for name in names:
    print(index, name)
    index += 1

# Better solution
for index, name in enumerate(names):
    print(index, name)
