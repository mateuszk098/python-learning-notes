'''
Communication with user with while loop.
'''

# Conditional statement to break
sen: str = ''
while sen != 'end':
    first_age: int = int(input('Enter your age: '))
    sen = input("Enter 'end' to quit: ")

print('Out first while.')

# Work control
counts: int = 0
while counts < 2:
    second_age: int = int(input('Enter your age: '))
    counts += 1

print('Out second while.')

# Break
while True:
    third_age: int = int(input('Enter your age: '))
    sen = input("Enter 'end' to quit: ")

    if sen == 'end':
        break

print('Out third while.')
