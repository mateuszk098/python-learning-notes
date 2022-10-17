'''
Sorting nested list by key.
'''

my_list: list[list[str | int]] = [['Bernice', 2], ['Angel', 1], ['Pat', 5], ['Shanna', 3]]
my_list.sort(key=lambda x: x[1])

print(my_list)
