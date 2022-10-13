'''
Create list and simple modification.
'''

guests: list = ['Nicola Kuhic', 'Raegan Pacocha', 'Geraldine Powlowski']

for guest in guests:
    print(f'I want to invite you to a dinner {guest}')

print(f'{guests[0]} cannot come.')
guests[0] = 'Gaylord Windler'

for guest in guests:
    print(f'I want to invite you to a dinner {guest}')
