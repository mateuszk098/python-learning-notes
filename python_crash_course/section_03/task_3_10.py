'''
List manipulation.
'''

cities: list = ['Łódź', 'Gdańsk', 'Warszawa', 'Wrocław']
print(f'Initial: {cities}')
cities.insert(0, 'Katowice')
print(f'After `insert`: {cities}')
cities.append('Kraków')
print(f'After `append`: {cities}')
cities.sort()
print(f'Sorted: {cities}')
cities.reverse()
print(f'Reversed: {cities}')
cities[3] = 'Poznań'
print(f'Element change: {cities}')
del cities[1]
print(f'Remove element: {cities}')
cities.pop()
print(f'Remove last element: {cities}')
