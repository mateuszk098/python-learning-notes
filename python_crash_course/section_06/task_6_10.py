'''
Embedd tuples in dictionary.
'''

favorite_numbers: dict = {'Kacie': (1, 2, 3),
                          'Jordy': (1,),
                          'Jeffrey': (99, 12)}

for person, numbers in favorite_numbers.items():
    print(f"{person} favourite numbers are:")
    for number in numbers:
        print(number, end=' ')
    print('\n')
