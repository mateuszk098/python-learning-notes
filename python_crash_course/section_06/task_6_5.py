'''
Create dictionary.
'''

# Dictionary (key: value)
rivers: dict = {'Vistula': 'Poland', 'Nile': 'Egypt', 'Amazon': 'Brasil'}

for river, country in rivers.items():
    print(f"{river} is in the {country}")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
