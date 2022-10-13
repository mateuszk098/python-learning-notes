'''
Simple exception handling.
'''

while True:
    a: str = input('Enter a or "q" to exit: ')
    if a == 'q':
        break

    b: str = input('Enter b or "q" to exit: ')
    if b == 'q':
        break

    try:
        num_a: int = int(a)
        num_b: int = int(b)
    except ValueError:
        print('Invalid number!')
    else:
        sum_ab: int = num_a + num_b
        print(f'Sum of a and b is {sum_ab}.')

print('Out of while.')
