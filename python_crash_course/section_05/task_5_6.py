'''
Conditional if-elif-else statements and checks.
'''

age: int = 18

if 0 < age < 2:
    print('You are a baby.')
elif 2 <= age < 4:
    print('You are a small child.')
elif 4 <= age < 13:
    print('You are a child.')
elif 13 <= age < 20:
    print('You are a teenager.')
elif 20 <= age < 65:
    print('You are an adult.')
elif age >= 65:
    print('You are at a certain age.')
else:
    print('Opps...')
