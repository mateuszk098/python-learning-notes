'''
Conditional statements with loops.
'''

numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number > 3:
        print(f'{number}st')
    elif number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    else:
        print('3rd')
