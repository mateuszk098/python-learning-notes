'''
Communication with user.
'''

number: int = int(input('Give me a number: '))

if number % 10 == 0:
    print(f'{number} is divisable by 10.')
else:
    print(f'{number} is not divisable by 10.')
