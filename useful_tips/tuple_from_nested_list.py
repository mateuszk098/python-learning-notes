'''
Create tuple of values from nested list.
'''

my_list: list[list[str | int]] = [['Bernice', 2], ['Angel', 1], ['Pat', 5], ['Shanna', 3]]
my_values: tuple[str | int, ...] = tuple(number for _, number in my_list)
print(my_values)

# Another method with zip
names, values = zip(*my_list)
print(values)
