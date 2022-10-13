'''
Communication with user.
'''

people: int = int(input('How many people do you foresee? '))

if people > 8:
    print('You have to wait a moment.')
else:
    print('We have a free table.')
