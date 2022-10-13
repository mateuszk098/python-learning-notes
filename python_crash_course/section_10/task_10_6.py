'''
Simple exception handling.
'''

try:
    num_a: int = int(input('Enter a: '))
    num_b: int = int(input('Enter b: '))
except ValueError:
    print('Invalid number!')
else:
    sum_ab: int = num_a + num_b
    print(f'Sum of a and b is {sum_ab}.')
