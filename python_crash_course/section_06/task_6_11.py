'''
Embedd dictionaries in dictionary.
'''

cities: dict = {'Madrid': {'Country': 'Spain', 'Population': 2_000_000},
                'Warsaw': {'Country': 'Poland', 'Population': 1_750_000}}

for city, informations in cities.items():
    print(f"Current city: {city}. Available informations:")
    for key, value in informations.items():
        print(f"{key} - {value}")
    print('\n')
