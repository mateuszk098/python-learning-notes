'''
Prints values from multiple lists using zip.
'''

names: list[str] = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes: list[str] = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes: list[str] = ["Marvel", "DC", "Marvel", "DC"]

# Yield tuples until an input is exhausted
for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} is actually {hero} from {universe} universe.")

# It's working like as a tuple
for value in zip(names, heroes, universes):
    print(value)
