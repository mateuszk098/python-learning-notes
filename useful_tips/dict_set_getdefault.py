'''
Attempt to get access to non-existing key.
'''

number_of_pets: dict[str, int] = {'dogs': 2}

# GET VALUE FOR KEY

# Non-pythonic way
if 'cats' in number_of_pets:
    print(f"I have {number_of_pets['cats']} cats")
else:
    print("I have 0 cats.")

# Pythonic way - if dictionary doesn't contain 'cats' key, then 0 is returned
print(f"I have {number_of_pets.get('cats', 0)} cats.")

# SET VALUE FOR KEY

# Non-pythonic way
# if 'cats' not in number_of_pets:
#     number_of_pets['cats'] = 0
# number_of_pets['cats'] += 2
# print(number_of_pets)

# Pythonic way - if the key exists then do nothing, else set 0 for 'cats'.
number_of_pets.setdefault('cats', 0)
number_of_pets['cats'] += 2
print(number_of_pets)
